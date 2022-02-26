"""Test for Clearing Stop Characters."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.clear_stop_char import clear_stop_char

# ---------------------------- function definition ----------------------------


def test_clear_stop_char_without_stoplist():
    """Test for Clearing Stop Characters without stoplist."""
    input_text = "**ست سرم (با ميل لوئر*سوپا*"
    assert clear_stop_char(text=input_text) == "ست سرم با ميل لوئر*سوپا"


def test_clear_stop_char_with_stoplist():
    """Test for Clearing Stop Characters with stoplist."""
    input_text = "**ست سرم (با ميل لوئر*سوپا*"
    assert (
        clear_stop_char(text=input_text, stoplist=["\\*"])
        == "ست سرم \
با ميل لوئر سوپا"
    )


def test_clear_stop_char_with_exceptlist():
    """Test for Clearing Stop Characters with exceptlist."""
    input_text = "**ست سرم )با ميل لوئر*سوپا*"
    assert (
        clear_stop_char(text=input_text, exceptlist=["\\)"])
        == "ست سرم )با ميل لوئر*سوپا"
    )


def test_clear_stop_char_with_exceptlist_stoplist():
    """Test for Clearing Stop Characters with exceptlist and stoplist."""
    input_text = "**ست سرم )با ميل لوئر*سوپا*"
    assert (
        clear_stop_char(input_text, exceptlist=["\\)"], stoplist=["\\*"])
        == "ست سرم )با ميل لوئر سوپا"
    )


def test_clear_stop_char_halfspace():
    """Test for Clearing Stop Characters with halfspace."""
    input_text = "دانشگاه‌های ایران"
    assert clear_stop_char(input_text) == "دانشگاه های ایران"


def test_clear_stop_char_without_halfspace():
    """Test for Clearing Stop Characters without halfspace."""
    input_text = "/دانشگاه‌های ایران"
    assert (
        clear_stop_char(input_text, exceptlist=["\u200c"])
        == "دانشگاه‌\
های ایران"
    )


def test_clear_stop_char_with_replace_char():
    """Test for replace_char argument."""
    input_text = "ست سرم )با ميل لوئر سوپا"
    assert clear_stop_char(input_text, replace_char=".") == "ست سرم .با ميل لوئر سوپا"
