"""Replace Arabic characters."""
# ------------------------ Import libraries and functions ---------------------
from typing import Any

import re

from cleaning_utils.constants import DIACRITICS, DIGITS, LETTERS, NUNATIONS
from cleaning_utils.types import FunctionType

# ---------------------------- function definition ----------------------------


def replace_arabic_char(
    text: str,
    letter: bool = True,
    number: bool = True,
    nunation: bool = True,
    diacritic: bool = True,
) -> Any:
    """Replace Arabic characters.

    It is a general-purpose normalizer, which can replace Arabic letters with
    Persian letters (e.g., ك with ک). Also, it can replace Hindi numerals with
    Arabic numerals (e.g., ۰۱۲۳۴۵۶۷۸۹ with 0123456789). Moreover, it can
    clear the input string from arabic diacritics (e.g.,  َ ِ ُ ) or nunations
    (e.g.,  ً ٍ ٌ ْ ّ ).

    Args:
        text (str): Accepts only one element (i.e., scalar).
        letter (bool): To replace Arabic letters with Persian
            letters.
        number (bool): To replace Hindi numerals with Arabic
            numerals.
        nunation (bool): To remove Arabic nunations.
        diacritic (bool): To remove Arabic diacritics.

    Returns:
        A text variable of <class "str"> after removing specified characters.

    Examples:
        >>> input_text = "آنژيوکت 20 صورتي ك"
        >>> replace_arabic_char(input_text)
        'آنژیوکت 20 صورتی ک'
        >>> text = "مُسْتَقِيمٌ سلامُ مُتَمَكِّنًائ ۰۱۲۳۴۵۶۷۸۹ ؤإئأء موسیٰ"
        >>> replace_arabic_char(text)
        'مستقیم سلام متمکنای 0123456789 وایا موسی'
    """
    if any([letter, number, nunation, diacritic]):
        operators = list(
            k
            for k, v in {
                replace_arabic_letters: letter,
                replace_arabic_numbers: number,
                remove_arabic_nunations: nunation,
                remove_arabic_diacritics: diacritic,
            }.items()
            if v
        )
        return chain(operators.pop(0), *operators)(text)
    return text


def remove_arabic_nunations(text: str) -> str:
    """Removes Arabic nunations.

    It is a general-purpose normalizer, which can remove Arabic nunations.

    Args:
        text (str): the text to be cleaned.

    Returns:
        A text variable of <class "str"> after removing specified characters.

    Examples:
        >>> text = "مٌ"
        >>> replace_arabic_char(text)
        'م'
    """
    # -------------------------- Make regex pattern ---------------------------
    rep = {re.escape(k): v for k, v in NUNATIONS.items()}
    pattern = re.compile("|".join(rep.keys()))
    # ---------------------------- Exert Function -----------------------------
    clear_text: str = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    return clear_text


def remove_arabic_diacritics(text: str) -> str:
    """Removes Arabic diacritics.

    It is a general-purpose normalizer, which can remove Arabic diacritics.

    Args:
        text (str): the text to be cleaned.

    Returns:
        A text variable of <class "str"> after removing specified characters.

    Examples:
        >>> text = "مُسْ"
        >>> replace_arabic_char(text)
        'مس'
    """
    # -------------------------- Make regex pattern ---------------------------
    rep = {re.escape(k): v for k, v in DIACRITICS.items()}
    pattern = re.compile("|".join(rep.keys()))
    # ---------------------------- Exert Function -----------------------------
    clear_text: str = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    return clear_text


def replace_arabic_numbers(text: str) -> str:
    """Replaces Arabic numbers with English numbers.

    It is a general-purpose normalizer, which replaces Arabic numbers with English.

    Args:
        text (str): the text to be cleaned.

    Returns:
        A text variable of <class "str"> after removing specified characters.

    Examples:
        >>> text = "۰۱۲۳۴۵۶۷۸۹"
        >>> replace_arabic_char(text)
        '0123456789'
    """
    # -------------------------- Make regex pattern ---------------------------
    rep = {re.escape(k): v for k, v in DIGITS.items()}
    pattern = re.compile("|".join(rep.keys()))
    # ---------------------------- Exert Function -----------------------------
    clear_text: str = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    return clear_text


def replace_arabic_letters(text: str) -> str:
    """Replaces Arabic letters with Persian (i.e., Farsi) letters.

    It is a general-purpose normalizer, which replaces Arabic letters with Persian.

    Args:
        text (str): the text to be cleaned.

    Returns:
        A text variable of <class "str"> after removing specified characters.

    Examples:
        >>> text = "ك"
        >>> replace_arabic_char(text)
        'ک'
    """
    # -------------------------- Make regex pattern ---------------------------
    rep = {re.escape(k): v for k, v in LETTERS.items()}
    pattern = re.compile("|".join(rep.keys()))
    # ---------------------------- Exert Function -----------------------------
    clear_text: str = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    return clear_text


def chain(first: FunctionType, *rest: FunctionType) -> Any:
    """Chains functions."""
    # pylint: disable = no-value-for-parameter
    return lambda x: first(chain(*rest)(x) if rest else x)
