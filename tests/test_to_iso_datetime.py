"""Testing the to_iso_datetime function."""
# ------------------------ Import libraries and functions ---------------------
import datetime

import khayyam
import pytest

# from cleaning_utils.from_dict_to_iso import from_dict_to_iso
from cleaning_utils.to_iso_datetime import to_iso_datetime

# ---------------------------- function definition ----------------------------


def test_to_iso_datetime_date_wronginputs():
    """Tests the to_iso_datetime function where date input is missing."""
    time = "blahblahblah"
    date = "spam"

    assert to_iso_datetime(date=date, time=time) is None


def test_to_iso_datetime_date_input_wrong_dict_keys():
    """Tests the to_iso_datetime function where date input dictionary keys are wrong."""
    date = {"hours": 23, "minute": 5, "second": 25}
    time = {"hour": 23, "minute": 5, "second": 25}

    assert to_iso_datetime(date=date, time=time) is None


def test_to_iso_datetime_date_input_wrong_dict_values():
    """Tests where date input dictionary values are wrong."""
    date = {"month": 1, "year": 1399, "days": 4}
    time = {"hour": 23, "minute": 5, "second": 25}

    assert to_iso_datetime(date=date, time=time) is None


def test_to_iso_datetime_date_input_dict_jalali_pass():
    """Tests the to_iso_datetime function where date input dictionary passes."""
    date = {"month": 1, "year": 1399, "day": 4}
    time = {"hour": 23, "minute": 5, "second": 25}
    assert to_iso_datetime(date, time) == "2020-03-23T23:05:25"


def test_to_iso_datetime_date_input_dict_gregorian_pass():
    """Tests the to_iso_datetime function where date input dictionary passes."""
    date = {"month": 2, "year": 2021, "day": 6}
    time = {"hour": 23, "minute": 5, "second": 25}
    assert to_iso_datetime(date, time, jalali=False) == "2021-02-06T23:05:25"


def test_to_iso_datetime_date_input_dict_gregorian_pass2():
    """Tests the to_iso_datetime function where date input dictionary passes."""
    date = {"month": 2, "year": 2021, "day": 6}
    time = {"hour": 23, "minute": 5, "second": 25}
    assert (
        to_iso_datetime(date, time, jalali=False, timezone=True)
        == "2021-02-06T23:05:25+03:26"
    )


def test_to_iso_datetime_input_datetime_date_pass():
    """Tests the to_iso_datetime function where date input datetime.date passes."""
    date = datetime.date(2015, 7, 22)
    time = datetime.time(0, 0, 0, 0)
    assert to_iso_datetime(date, time) == "2015-07-22T00:00:00"


def test_to_iso_datetime_input_jalalidate_date_pass():
    """Tests where date input khayyam.jalali_date.JalaliDate passes."""
    date = khayyam.JalaliDate(1394, 4, 31)
    time = khayyam.jalali_datetime.JalaliDatetime(hour=0, minute=0, second=0)
    assert to_iso_datetime(date, time) == "2015-07-22T00:00:00"


def test_to_iso_datetime_time_input_wrong_dict_keys():
    """Tests where time input dictionary keys are wrong."""
    date = {"month": 1, "year": 1399, "day": 4}
    time = {"hr": 0, "min": 1, "sec": 0}

    assert to_iso_datetime(date=date, time=time) is None


def test_to_iso_datetime_time_input_wrong_dict_values():
    """Tests where time input dictionary values are wrong."""
    date = {"month": "1", "year": "1399", "days": "4"}
    time = {"hour": "0", "minute": "1", "second": "0"}

    assert to_iso_datetime(date=date, time=time) is None


def test_to_iso_datetime_time_input_jalali_dict_pass():
    """Tests where time input dictionary for Jalali calendar passes."""
    date = {"month": 4, "year": 1399, "day": 31}
    time = {"hour": 15, "minute": 38, "second": 6}
    assert to_iso_datetime(date=date, time=time, jalali=True) == "2020-07-21T15:38:06"


def test_to_iso_datetime_time_input_greg_tz_dict_pass():
    """Tests where time input dictionary for Gregorian with tz calendar passes."""
    date = {"month": 4, "year": 2019, "day": 5}
    time = {"hour": 0, "minute": 0, "second": 0}
    assert (
        to_iso_datetime(date, time, jalali=False, timezone=False)
        == "2019-04-05T00:00:00"
    )


def test_to_iso_datetime_time_input_jalali_dict_pass_tz():
    """Tests where time input dictionary for Jalali calendar with tz passes."""
    date = {"month": 4, "year": 1399, "day": 31}
    time = {"hour": 15, "minute": 38, "second": 6}
    assert (
        to_iso_datetime(date=date, time=time, timezone=True)
        == "2020-07-21T15:38:06+03:26"
    )


def test_to_iso_date_time_input_jalali_dict_pass_tz():
    """Tests where date input dictionary for Jalali calendar with tz passes."""
    date = {"month": 4, "year": 1399, "day": 31}
    time = {"hour": 0, "minute": 0, "second": 0}
    assert (
        to_iso_datetime(date=date, time=time, timezone=True)
        == "2020-07-21T00:00:00+03:26"
    )


def test_to_iso_datetime_time_gregorian_input_dict_pass():
    """Tests where time input dictionary for Jalali calendar passes."""
    date = {"month": 2, "year": 2021, "day": 6}
    time = {"hour": 15, "minute": 38, "second": 6}
    assert to_iso_datetime(date=date, time=time, jalali=False) == "2021-02-06T15:38:06"


def test_to_iso_datetime_time_gregorian_input_dict_tz_pass():
    """Tests where time input dictionary for Jalali calendar with tz passes."""
    date = {"month": 2, "year": 2021, "day": 6}
    time = {"hour": 15, "minute": 38, "second": 6}
    assert (
        to_iso_datetime(date, time, jalali=False, timezone=True)
        == "2021-02-06T15:38:06+03:26"
    )


def test_to_iso_datetime_input_datetime_time_pass():
    """Tests where inputs datetime.date and datetime.time pass."""
    date = datetime.date(2015, 7, 22)
    time = datetime.time(15, 38, 6, 37269)
    assert to_iso_datetime(date, time) == "2015-07-22T15:38:06.037269"


def test_to_iso_datetime_input_datetime_time_tz_pass():
    """Tests where inputs datetime.date and datetime.time with tz pass."""
    date = datetime.date(2015, 7, 22)
    time = datetime.time(15, 38, 6, 37269)
    assert to_iso_datetime(date, time) == "2015-07-22T15:38:06.037269"


def test_to_iso_datetime_input_jalalidatetime_time_pass():
    """Tests where inputs khayyam.jalali_date.JalaliDate JalaliDatetime pass."""
    date = khayyam.JalaliDate(1394, 4, 31)
    time = khayyam.JalaliDatetime(1394, 4, 31, 15, 38, 6, 37269)
    assert to_iso_datetime(date, time) == "2015-07-22T15:38:06.037269"


def test_to_iso_datetime_input_jalalidatetime_tz_time_pass():
    """Tests where inputs khayyam.jalali_date.JalaliDate and JalaliDatetime pass."""
    date = khayyam.JalaliDate(1394, 4, 31)
    time = khayyam.JalaliDatetime(1394, 4, 31, 15, 38, 6, 37269)
    assert (
        to_iso_datetime(date=date, time=time, timezone=True)
        == "2015-07-22T15:38:06.037269+03:26"
    )


def test_to_iso_datetime_input_jalalidatetime_tz_time_pass2():
    """Tests where inputs khayyam.jalali_date.JalaliDate and datetime.time pass."""
    date = khayyam.jalali_date.JalaliDate(1394, 4, 31)
    time = khayyam.JalaliDatetime(hour=0, minute=0, second=0)
    assert (
        to_iso_datetime(date=date, time=time, timezone=True)
        == "2015-07-22T00:00:00+03:26"
    )


def test_to_iso_datetime_time_input_wrong_dict_values2():
    """Tests where date input dictionary values are wrong."""
    date = {"month": 1, "year": 1399, "day": 4}
    time = {"hour": 23, "minute": "5", "second": "25"}
    with pytest.raises(Exception) as execinfo:
        to_iso_datetime(date=date, time=time)

    assert execinfo.value.args[0] == "an integer is required (got type str)"


def test_to_iso_datetime_time_input_wrong_dict_values3():
    """Tests where date input dictionary values are wrong."""
    date = {"month": 1, "year": 1399, "day": 4}
    time = {"hour": "23", "minute": "5", "second": "25"}
    with pytest.raises(Exception) as execinfo:
        to_iso_datetime(date=date, time=time)

    assert execinfo.value.args[0] == "an integer is required (got type str)"


def test_to_iso_date_dict_none_time_pass():
    """Tests the to_iso_datetime function where date is dict and time input is None."""
    date = {"month": 2, "year": 2021, "day": 6}
    assert (
        to_iso_datetime(date=date, jalali=False, timezone=True)
        == "2021-02-06T00:00:00+03:26"
    )


def test_to_iso_date_datetime_none_time_pass():
    """Tests where date is datetime and time input is None."""
    date = datetime.date(2015, 7, 22)
    assert (
        to_iso_datetime(date=date, jalali=False, timezone=True)
        == "2015-07-22T00:00:00+03:26"
    )


def test_to_iso_date_khayyam_none_time_pass():
    """Tests where date is khayyam and time input is None."""
    date = khayyam.JalaliDate(1394, 4, 31)
    assert (
        to_iso_datetime(date=date, jalali=False, timezone=False)
        == "2015-07-22T00:00:00"
    )
