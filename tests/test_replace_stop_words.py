"""Testing the replace_stop_words function."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.replace_stop_words import replace_stop_words

# ---------------------------- function definition ----------------------------


def test_replace_stop_words_pass():
    """Test passes for replace_stop_words."""
    input_text = "Welcome to the lovely vlg of Budleigh Babberton"
    assert (
        replace_stop_words(input_text, stop=["vlg"], replace=["village"])
        == "Welcome to the lovely village of Budleigh Babberton"
    )
