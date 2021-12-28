"""Cleaning Numbers Characters."""
# ------------------------ Import libraries and functions ---------------------
import re

from cleaning_utils.constants import NUM_SEPERATED, NUM_SEPERATOR
from cleaning_utils.space_cleaner import space_cleaner

# ---------------------------- function definition ----------------------------


def number_separator(text: str) -> str:
    """Separates numbers from text with spaces.

    It is a general-purpose number normalizer, which can separate numbers
    which are sticked to the surrounding text. It recognizes English numbers
    (e.g., with 1,2,3).

    Args:
        text (str): the text to be cleaned.

    Returns:
        A text variable of <class 'str'> after separating numbers.

    Examples:
        >>> number_separator("hello2 people")
        'hello 2 people'

    """
    clear_text = space_cleaner(re.sub(NUM_SEPERATOR, NUM_SEPERATED, text))
    return clear_text
