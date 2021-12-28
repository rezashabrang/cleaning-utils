"""Constants."""
from typing import Any, Dict, Set

TIME_SET: Set[Any] = set({"year", "month", "day", "hour", "minute", "second"})
DATE_SET: Set[Any] = set({"year", "month", "day"})
ISO_PATTERN: str = r"^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$"
LETTERS: Dict[str, str] = dict(
    {
        "ي": "ی",
        "ك": "ک",
        "دِ": "د",
        "بِ": "ب",
        "زِ": "ز",
        "ذِ": "ذ",
        "شِ": "ش",
        "سِ": "س",
        "ى": "ی",
        "ئ": "ی",  # Arabic Letter Yeh With Hamza Above
        "إ": "ا",  # Arabic Letter Alef With Hamza Below
        "ؤ": "و",  # Arabic Letter Waw With Hamza Above
        "أ": "ا",  # Arabic Letter Alef With Hamza Above
        "ء": "",  # Arabic Letter Hamza
        "\u0654": "",  # Arabic Hamza Above
        "\u0655": "",  # Arabic Hamza Below
        "\u0629": "ه",  # Arabic Letter Teh Marbuta
        "\u066A": "%",  # Arabic Percent Sign
        "\u06C0": "ه",  # Arabic Letter Heh With Yeh Above
    },
)
DIGITS: Dict[str, str] = dict(
    {
        # persian digits
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9",
        # arabic digits
        "٠": "0",
        "١": "1",
        "٢": "2",
        "٣": "3",
        "٤": "4",
        "٥": "5",
        "٦": "6",
        "٧": "7",
        "٨": "8",
        "٩": "9",
    },
)
NUNATIONS: Dict[str, str] = dict(
    {
        "\u064B": "",  # Arabic Fathatan
        "\u064C": "",  # Arabic Dammatan
        "\u064D": "",  # Arabic Kasratan
        "\u0651": "",  # Arabic Shadda
        "\u0652": "",  # Arabic Sukun
        "\u0670": "",  # Arabic Letter Superscript Alef
        "\u0656": "",  # Arabic Subscript Alef
    },
)
DIACRITICS: Dict[str, str] = dict(
    {
        "\u0618": "",  # Arabic Small Fatha
        "\u064E": "",  # Arabic Fatha
        "\u0619": "",  # Arabic Small Damma
        "\u064F": "",  # Arabic Damma
        "\u061A": "",  # Arabic Small Kasra
        "\u0650": "",  # Arabic Kasra
    },
)
NUM_SEPERATOR = r"([0-9]+|[0-9]+)"
NUM_SEPERATED = " " + r"\1" + " "
STOP = [
    " ک ",
    " پ ",
    " خ ",
    " ب ",
    " م ",
    " ش ",
    " ط ",
    " تهران استان تهران شهرستان تهران ",
    "فاز",
]
REPLACE = [
    " کوچه ",
    " پلاک ",
    " خیابان ",
    " بلوار ",
    " میدان ",
    " شهید ",
    " طبقه ",
    " استان تهران شهرستان تهران ",
    " فاز ",
]
