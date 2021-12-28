"""Address cleaner."""
# ------------------------ Import libraries and functions ---------------------
# from typing import Optional

from cleaning_utils.clear_stop_char import clear_stop_char
from cleaning_utils.constants import REPLACE, STOP
from cleaning_utils.number_separator import number_separator
from cleaning_utils.remove_duplicate_words import remove_duplicate_words
from cleaning_utils.replace_arabic_char import replace_arabic_char
from cleaning_utils.replace_stop_words import replace_stop_words
from cleaning_utils.space_cleaner import space_cleaner

# ---------------------------- function definition ----------------------------


def address_cleaner(
    text: str,
    province: str = "",
    city: str = "",
) -> str:
    """Address cleaner.

    It is a specific function, which can clear Iranian address text to be
    used in geocode services.

    Args:
        text (str): Accepts only one element (i.e., scalar).
        province (str): If added, the province name will be added at the beginning of
                the text.
        city (str): If added, the city name will be added at the beginning of the text.

    Returns:
        A text variable of <class "str"> after cleaning address text.

    Examples:
        >>> input_text = "خ مفتح شمالي ک درفش پ3 و4"
        >>> address_cleaner(input_text, city="تهران")
        'تهران خیابان مفتح شمالی کوچه درفش پلاک 3 و 4'

    """
    cleaned_text = clear_stop_char(text)
    cleaned_text = replace_stop_words(cleaned_text, stop=STOP, replace=REPLACE)
    cleaned_text = replace_arabic_char(cleaned_text)
    cleaned_text = number_separator(cleaned_text)
    cleaned_text = replace_stop_words(cleaned_text, stop=STOP, replace=REPLACE)
    cleaned_text = clear_stop_char(cleaned_text)
    cleaned_text = city + " " + cleaned_text
    cleaned_text = province + " " + cleaned_text
    cleaned_text = replace_stop_words(cleaned_text, stop=STOP, replace=REPLACE)
    cleaned_text = clear_stop_char(cleaned_text)
    cleaned_text = remove_duplicate_words(cleaned_text)
    return space_cleaner(cleaned_text)
