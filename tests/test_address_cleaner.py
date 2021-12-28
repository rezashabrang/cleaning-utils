"""Testing the address_cleaner function."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.address_cleaner import address_cleaner

# ---------------------------- function definition ----------------------------


def test_address_cleaner_pass_city():
    """Test passes for address_cleaner, where city is provided."""
    input_text = "خ مفتح شمالي ک درفش پ3 و4"
    assert (
        address_cleaner(text=input_text, city="تهران")
        == "تهران خیابان مفتح شمالی کوچه درفش پلاک 3 و 4"
    )


def test_address_cleaner_pass_province():
    """Test passes for address_cleaner, where province is provided."""
    input_text = "خ مفتح شمالي ک درفش پ3 و4"
    assert (
        address_cleaner(text=input_text, province="استان تهران")
        == "استان تهران خیابان مفتح شمالی کوچه درفش پلاک 3 و 4"
    )


def test_address_cleaner_pass_without_province_or_city():
    """Test passes for address_cleaner, where city or province are not provided."""
    input_text = "خ مفتح شمالي ک درفش پ3 و4"
    assert (
        address_cleaner(text=input_text)
        == "خیابان مفتح شمالی\
 کوچه درفش پلاک 3 و 4"
    )
