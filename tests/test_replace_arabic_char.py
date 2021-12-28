"""Test Replace Arabic characters."""
# ------------------------ Import libraries and functions ---------------------
from cleaning_utils.replace_arabic_char import replace_arabic_char

# ---------------------------- function definition ----------------------------


def test_replace_arabic_char_empty():
    """Test Replace Arabic characters where none of arguments are used by the user."""
    input_text = "آنژيوکت 20 صورتي"
    assert replace_arabic_char(input_text) == "آنژیوکت 20 صورتی"


def test_replace_arabic_char_all_false():
    """Test where all of arguments are set false by the user."""
    input_text = "مُسْتَقِيمٌ سلامُ مُتَمَكِّنًائ ۰۱۲۳۴۵۶۷۸۹ ؤإئأء موسیٰ"
    assert (
        replace_arabic_char(
            input_text,
            letter=False,
            number=False,
            nunation=False,
            diacritic=False,
        )
        == "مُسْتَقِيمٌ سلامُ مُتَمَكِّنًائ ۰۱۲۳۴۵۶۷۸۹ ؤإئأء موسیٰ"
    )


def test_replace_arabic_char_number_true():
    """Test where only `number` is set True by the user."""
    input_text = "مُسْتَقِيمٌ سلامُ مُتَمَكِّنًائ ۰۱۲۳۴۵۶۷۸۹ ؤإئأء موسیٰ"
    assert (
        replace_arabic_char(
            input_text,
            letter=False,
            number=True,
            nunation=False,
            diacritic=False,
        )
        == "مُسْتَقِيمٌ سلامُ مُتَمَكِّنًائ 0123456789 ؤإئأء موسیٰ"
    )


def test_replace_arabic_char_letter_true():
    """Test where only `letter` is set True by the user."""
    input_text = "مُسْتَقِيمٌ سلامُ مُتَمَكِّنًائ ۰۱۲۳۴۵۶۷۸۹ ؤإئأء موسیٰ"
    assert (
        replace_arabic_char(
            input_text,
            letter=True,
            number=False,
            nunation=False,
            diacritic=False,
        )
        == "مُسْتَقِیمٌ سلامُ مُتَمَکِّنًای ۰۱۲۳۴۵۶۷۸۹ وایا موسیٰ"
    )


def test_replace_arabic_char_nunation_true():
    """Test where only `nunation` is set True by the user."""
    input_text = "مُسْتَقِيمٌ سلامُ مُتَمَكِّنًائ ۰۱۲۳۴۵۶۷۸۹ ؤإئأء موسیٰ"
    assert (
        replace_arabic_char(
            input_text,
            letter=False,
            number=False,
            nunation=True,
            diacritic=False,
        )
        == "مُستَقِيم سلامُ مُتَمَكِنائ ۰۱۲۳۴۵۶۷۸۹ ؤإئأء موسی"
    )


def test_replace_arabic_char_diacritic_true():
    """Test Replace Arabic characters where only `diacritic` is set True by the user."""
    input_text = "مُسْتَقِيمٌ سلامُ مُتَمَكِّنًائ ۰۱۲۳۴۵۶۷۸۹ ؤإئأء موسیٰ"
    assert (
        replace_arabic_char(
            input_text,
            letter=False,
            number=False,
            nunation=False,
            diacritic=True,
        )
        == "مسْتقيمٌ سلام متمكّنًائ ۰۱۲۳۴۵۶۷۸۹ ؤإئأء موسیٰ"
    )
