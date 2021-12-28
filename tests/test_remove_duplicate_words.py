"""Testing the remove_duplicate_words function."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.remove_duplicate_words import remove_duplicate_words

# ---------------------------- function definition ----------------------------


def test_remove_duplicate_words_pass():
    """Test passes for remove_duplicate_words."""
    input_text = "Potter Potter I have a message for you"
    assert (
        remove_duplicate_words(input_text)
        == """Potter I have a message for\
 you"""
    )


def test_remove_duplicate_words_pass2():
    """Test passes for remove_duplicate_words."""
    input_text = "Hey Potter, Potter, I have a message for you"
    assert (
        remove_duplicate_words(input_text)
        == """Hey Potter, I have a\
 message for you"""
    )
