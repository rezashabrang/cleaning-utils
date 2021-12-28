"""Persian Numbers Format."""
# ------------------------ Import libraries and functions ---------------------
from typing import Union

import re

# ---------------------------- function definition ----------------------------


def to_fa_numbers(number: Union[int, float, str]) -> str:
    """Farsi number format.

    It is a general-purpose number formatter, which relaces Arabic numbers
    with Persian ones.

    Args:
        number (int or float or str): Accepts only one element (i.e., scalar).

    Returns:
        A text variable of <class 'str'> after making Persian numbers.

    Examples:
        >>> to_fa_numbers(165485613)
        '۱۶۵۴۸۵۶۱۳'


    """
    digits = {
        # Persian digits
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
        # ",": "،"
    }
    rep_digits = {re.escape(k): v for k, v in digits.items()}
    pattern_digits = re.compile("|".join(rep_digits.keys()))
    clear_text = pattern_digits.sub(
        lambda m: rep_digits[re.escape(m.group(0))],
        str(number),
    )
    return clear_text
