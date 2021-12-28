"""Testing the number_separator function."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.number_separator import number_separator

# ---------------------------- function definition ----------------------------


def test_number_separator_pass():
    """Test passes for number_separator."""
    input_text = "hello2 people"
    assert number_separator(input_text) == "hello 2 people"
