"""Initiates Package."""
from .address_cleaner import address_cleaner
from .clear_stop_char import clear_stop_char, strip_stars
from .datetime_diff import datetime_diff
from .from_datetime_to_iso import from_datetime_to_iso
from .from_dict_to_iso import (
    from_dict_to_iso,
    from_gregorian_dict_to_iso,
    from_jalali_dict_to_iso,
)
from .from_khayyam_to_iso import from_khayyam_to_iso
from .human_number import human_number
from .number_separator import number_separator
from .remove_duplicate_words import remove_duplicate_words
from .replace_arabic_char import (
    chain,
    remove_arabic_diacritics,
    remove_arabic_nunations,
    replace_arabic_char,
    replace_arabic_letters,
    replace_arabic_numbers,
)
from .replace_stop_words import replace_stop_words
from .space_cleaner import space_cleaner
from .to_fa_numbers import to_fa_numbers
from .to_iso_datetime import to_iso_datetime

__version__ = "0.1.4"
__all__ = [
    "clear_stop_char",
    "replace_arabic_char",
    "datetime_diff",
    "to_iso_datetime",
    "number_separator",
    "replace_stop_words",
    "remove_duplicate_words",
    "address_cleaner",
    "human_number",
    "to_fa_numbers",
    "from_datetime_to_iso",
    "from_dict_to_iso",
    "from_khayyam_to_iso",
    "chain",
    "replace_arabic_letters",
    "replace_arabic_numbers",
    "remove_arabic_diacritics",
    "remove_arabic_nunations",
    "from_gregorian_dict_to_iso",
    "from_jalali_dict_to_iso",
    "space_cleaner",
    "strip_stars",
]
