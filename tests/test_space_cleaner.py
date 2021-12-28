"""Testing the space_cleaner function."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.space_cleaner import space_cleaner

# ---------------------------- function definition ----------------------------


def test_space_cleaner():
    """Test passes for number_separator."""
    input_text = "hello to  people "
    assert space_cleaner(input_text) == "hello to people"
