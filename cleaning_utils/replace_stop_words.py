"""Replace Stop Words."""
# ------------------------ Import libraries and functions ---------------------
from typing import Iterable

import re

# ---------------------------- function definition ----------------------------


def replace_stop_words(
    text: str,
    stop: Iterable[str],
    replace: Iterable[str],
) -> str:
    """Replace stop words.

    It is a general-purpose function, which can replace specific words with
    desired ones, or remove them. It receives a list of stop words and another
    list of replace words.

    Args:
        text (str): Accepts only one element (i.e., scalar).
        stop (list, default None):
            List of words which are going to be filtered out.
        replace (list, default None): List of replace words.

    Returns:
        A text variable of <class 'str'> after removing stop words.

    Examples:
        >>> input_text = "Welcome to the lovely vlg of Budleigh Babberton"
        >>> replace_stop_words(input_text, stop=['vlg'], replace=['village'])
        'Welcome to the lovely village of Budleigh Babberton'

    """
    stop = [str(i) for i in stop]
    replace = [str(i) for i in replace]
    rep = dict(zip(stop, replace))
    rep = {re.escape(k): v for k, v in rep.items()}
    return re.compile("|".join(rep.keys())).sub(
        lambda m: rep[re.escape(m.group(0))],
        text,
    )


def clear_stop_words(
    text: str, stop_list: Iterable[str], replace_char: str = " "
) -> str:
    """Replace stop words with specified replace character."""
    pattern = "|".join(stop_list)
    # ---------------------------- Exert Function -----------------------------
    clear_text = re.sub(pattern, replace_char, text)

    return clear_text
