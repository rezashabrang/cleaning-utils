"""Testing the datetime_diff function."""
# ------------------------ Import libraries and functions ---------------------
import datetime

import pytest

from cleaning_utils.datetime_diff import datetime_diff

# ---------------------------- function definition ----------------------------


def test_datetime_diff_input_error():
    """Tests the datetime_diff function where input is wrong."""
    datetime1 = 2020
    datetime2 = 2021
    with pytest.raises(Exception) as execinfo:
        datetime_diff(datetime1, datetime2)

    assert execinfo.value.args[0] == "unknown datetime formats"


def test_datetime_diff_iso_string_pass():
    """Tests the datetime_diff function where both inputs are valid iso ISO 8601."""
    datetime1 = "2020-03-23T23:05:25+03:26"
    datetime2 = "2020-03-27T00:01:00+03:26"
    assert datetime_diff(datetime1, datetime2) == datetime.timedelta(
        days=3,
        seconds=3335,
    )


def test_datetime_diff_iso_string_error():
    """Tests the datetime_diff function where inputs are not valid iso ISO 8601."""
    datetime1 = "2020-03-23T2"
    datetime2 = "2020-03-27T00:01:00+0"
    with pytest.raises(Exception) as execinfo:
        datetime_diff(datetime1, datetime2)

    assert execinfo.value.args[0] == "unknown datetime formats"


def test_datetime_diff_dict_pass_full_equal():
    """Testsfunction where inputs are valid dictionaries with full datetime date."""
    datetime1 = {
        "month": 1,
        "year": 1399,
        "day": 4,
        "hour": 23,
        "minute": 5,
        "second": 25,
    }
    datetime2 = {
        "month": 1,
        "year": 1399,
        "day": 8,
        "hour": 0,
        "minute": 1,
        "second": 0,
    }
    assert datetime_diff(datetime1, datetime2) == datetime.timedelta(
        days=3,
        seconds=3335,
    )


def test_datetime_diff_dict_error_full_equal():
    """Tests where inputs are not valid dictionaries with full datetime date."""
    ddd = {"month": 1, "year": 1399, "day": 4, "hour": 23, "min": 5, "sec": 25}
    eee = {"month": 1, "year": 1399, "day": 8, "hour": 0, "minute": 1, "sec": 0}
    with pytest.raises(Exception) as execinfo:
        datetime_diff(ddd, eee)

    assert execinfo.value.args[0] == "unknown datetime formats"


def test_date_diff_dict_pass():
    """Tests where inputs are valid dictionaries with date data."""
    datetime1 = {"month": 1, "year": 1399, "day": 4}
    datetime2 = {"month": 1, "year": 1399, "day": 8}
    assert datetime_diff(datetime1, datetime2) == datetime.timedelta(days=4)


def test_date_diff_dict_error():
    """Tests where inputs are not valid dictionaries with date data."""
    datetime1 = {"month": 1, "year": 1399, "days": 4}
    datetime2 = {"month": 1, "years": 1399, "day": 8}
    with pytest.raises(Exception) as execinfo:
        datetime_diff(datetime1, datetime2)

    assert execinfo.value.args[0] == "unknown datetime formats"


def test_datetime_diff_dict_error():
    """Tests the datetime_diff function."""
    dt1 = {"month": 1, "year": 1399, "hour": 23, "minute": 5, "second": 25}
    dt2 = {"year": 1399, "day": 8, "hour": 0, "minute": 1, "second": 0}
    with pytest.raises(Exception) as execinfo:
        datetime_diff(dt1, dt2)

    assert execinfo.value.args[0] == "unknown datetime formats"


# def test_datetime_diff_dict_pass_full_unequal():
#     """Tests the datetime_diff function"""
#     datetime1 = {
#         "month": 1,
#         "year": 1399,
#         "day": 4,
#         "hour": 23
#     }
#     datetime2 = {
#         "month": 1,
#         "year": 1399,
#         "day": 8
#     }
#     assert datetime_diff(datetime1, datetime2) == datetime.timedelta(
#         days=3, seconds=3335
#     )
