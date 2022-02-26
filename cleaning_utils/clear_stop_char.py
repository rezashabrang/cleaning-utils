"""Clearing Stop Characters."""
# ------------------------ Import libraries and functions ---------------------
from typing import Iterable, List, Optional

import re

from cleaning_utils.space_cleaner import space_cleaner

# ---------------------------- function definition ----------------------------


def clear_stop_char(
    text: str,
    stoplist: Optional[List[str]] = None,
    exceptlist: Optional[List[str]] = None,
    replace_char: str = " ",
) -> str:
    r"""Clearing Stop Characters.

    It is a general-purpose function for removing stop characters.

    Args:
        text (str): Accepts only one element (i.e., scalar).
        stoplist (list, default None): Accepts a list of extra stop
            characters, should escape special regex characters
            (e.g., stoplist=['\\*']).
        exceptlist (list, default None): Accepts a list of exceptions,
            should escape special regex characters
            (e.g., exceptlist=['\\?']).
        replace_char (str): Replacing the stop characters with a character
            of choosing.

    Returns:
        A text variable of <class 'str'> after removing specified characters.

    Examples:
        >>> input_text = '**device 15*6 cm Some Company / IR**'
        >>> clear_stop_char(input_text)
        'device 15*6 cm Some Company IR'
        >>> input_text = '**ست سرم (با ميل لوئر*سوپا*'
        >>> clear_stop_char(input_text, stoplist = ['\\*'])
        'ست سرم با ميل لوئر سوپا'
        >>> input_text = 'دانشگاه‌های ایران/'
        >>> clear_stop_char(input_text, exceptlist=[u'\u200c'])
        'دانشگاه‌های ایران'

    """
    reps = prepare_stop_char_list(stoplist=stoplist, exceptlist=exceptlist)
    # -------------------------- Make regex pattern ---------------------------
    pattern = "|".join(reps)
    # ---------------------------- Exert Function -----------------------------
    clear_text = re.sub(pattern, replace_char, text)
    # replace double space with single space

    # strip leading and trailing stars but keep middle chars
    clear_text = strip_stars(clear_text)
    # strip leading and trailing spaces
    clear_text = " " + clear_text + " "
    clear_text = space_cleaner(clear_text)
    return clear_text


def prepare_stop_char_list(
    stoplist: Optional[List[str]] = None,
    exceptlist: Optional[List[str]] = None,
) -> Iterable[str]:
    """Prepares the list of stop characters."""
    # ---------------------------- Exert Arguments ----------------------------
    if stoplist:
        if exceptlist:
            reps = stoplist + [
                "\\/",
                "\u060C",  # Arabic comma
                "\u200c",  # halfspace
                "\\[",
                "\\]",
                "\\:",
                "\\|",
                '\\"',
                "\\?",
                "\\<",
                "\\>",
                "\\,",
                "\\(",
                "\\)",
                "\\\\",
                "\\.",
                "\\+",
                "\\-",
                "\\!",
                "\\$",
                "\\`",
                "\\،",
                "\\_",
                "\\{",
                "\\}",
                '"',
                "\\؛",
                "\\«",
                "\\»",
                "\\;",
                "\\—" "\\“",
                "\\”" "\\‘",
                "\\’",
            ]
            removes_exceptions_from_list(lister=reps, exceptlist=exceptlist)
        else:
            reps = stoplist + [
                "\\/",
                "\u060C",  # Arabic comma
                "\u200c",  # halfspace
                "\\[",
                "\\]",
                "\\:",
                "\\|",
                '\\"',
                "\\?",
                "\\<",
                "\\>",
                "\\,",
                "\\(",
                "\\)",
                "\\\\",
                "\\.",
                "\\+",
                "\\-",
                "\\!",
                "\\$",
                "\\`",
                "\\،",
                "\\_",
                "\\{",
                "\\}",
                '"',
                "\\؛",
                "\\«",
                "\\»",
                "\\;",
                "\\—" "\\“",
                "\\”" "\\‘",
                "\\’",
            ]
    else:
        if exceptlist:
            reps = [
                "\\/",
                "\u060C",  # Arabic comma
                "\u200c",  # halfspace
                "\\[",
                "\\]",
                "\\:",
                "\\|",
                '\\"',
                "\\?",
                "\\<",
                "\\>",
                "\\,",
                "\\(",
                "\\)",
                "\\\\",
                "\\.",
                "\\+",
                "\\-",
                "\\!",
                "\\$",
                "\\`",
                "\\،",
                "\\_",
                "\\{",
                "\\}",
                '"',
                "\\؛",
                "\\«",
                "\\»",
                "\\;",
                "\\—" "\\“",
                "\\”" "\\‘",
                "\\’",
            ]
            removes_exceptions_from_list(lister=reps, exceptlist=exceptlist)
        else:
            reps = [
                "\\/",
                "\u060C",  # Arabic comma
                "\u200c",  # halfspace
                "\\[",
                "\\]",
                "\\:",
                "\\|",
                '\\"',
                "\\?",
                "\\<",
                "\\>",
                "\\,",
                "\\(",
                "\\)",
                "\\\\",
                "\\.",
                "\\+",
                "\\-",
                "\\!",
                "\\$",
                "\\`",
                "\\،",
                "\\_",
                "\\{",
                "\\}",
                '"',
                "\\؛",
                "\\«",
                "\\»",
                "\\;",
                "\\—" "\\“",
                "\\”" "\\‘",
                "\\’",
            ]
    return reps


def strip_stars(text: str) -> str:
    """Strips trailing and leading star characters.

    Args:
        text (str): the text to be cleaned.

    Returns:
        A text variable of <class 'str'> after separating numbers.

    Examples:
        >>> strip_stars("*hello to people**")
        'hello to people'

    """
    return text.strip("**").strip("*")


def removes_exceptions_from_list(
    lister: List[str],
    exceptlist: List[str],
) -> List[str]:
    """Removes exceptions from a list."""
    # ---------------------------- Exert Arguments ----------------------------
    reps = lister
    for i in exceptlist:
        reps.remove(i)
    return lister
