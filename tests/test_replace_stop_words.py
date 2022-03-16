"""Testing the replace_stop_words function."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.replace_stop_words import clear_stop_words, replace_stop_words

# ---------------------------- function definition ----------------------------


def test_replace_stop_words_pass():
    """Test passes for replace_stop_words."""
    input_text = "Welcome to the lovely vlg of Budleigh Babberton"
    assert (
        replace_stop_words(input_text, stop=["vlg"], replace=["village"])
        == "Welcome to the lovely village of Budleigh Babberton"
    )


def test_clear_stop_words_general():
    """General test for function for replacing stop words"""
    input_text = "دیر آمدی که دست از دامنت ندارم."
    output = clear_stop_words(text=input_text, stop_list=["از", "که"], replace_char=".")
    expected = "دیر آمدی . دست . دامنت ندارم."

    assert output == expected
