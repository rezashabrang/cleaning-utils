"""Testing the human_number function."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.human_number import human_number

# ---------------------------- function definition ----------------------------


def test_human_number_pass():
    """Test passes for human_number."""
    assert human_number(165485613) == "165,485,613"
