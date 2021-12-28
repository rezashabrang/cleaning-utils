"""Testing the to_fa_numbers function."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.to_fa_numbers import to_fa_numbers

# ---------------------------- function definition ----------------------------


def test_to_fa_numbers_pass():
    """Test passes for to_fa_numbers."""
    assert to_fa_numbers(165485613) == "۱۶۵۴۸۵۶۱۳"


def test_to_fa_numbers_pass2():
    """Test passes for to_fa_numbers."""
    assert to_fa_numbers(1654.85613) == "۱۶۵۴.۸۵۶۱۳"


def test_to_fa_numbers_pass3():
    """Test passes for to_fa_numbers."""
    assert to_fa_numbers("1654.85613") == "۱۶۵۴.۸۵۶۱۳"


def test_to_fa_numbers_pass4():
    """Test passes for to_fa_numbers."""
    assert to_fa_numbers("باید برویم خیابان 64") == "باید برویم خیابان ۶۴"
