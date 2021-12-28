"""Makes a ISO 8601 datetime string from dictionaries."""
# ------------------------ Import libraries and functions ---------------------
from typing import Any, Dict, Mapping, Optional

import datetime

import khayyam
import pytz

# ---------------------------- function definition ----------------------------


def valid_date_dict(function):
    """A decorator function to check whether the date input is valid."""

    def wrapper(*args, **kw):
        if not {"year", "month", "day"} <= kw["date"].keys():
            # ----------------------- return the actual function ----------------------
            return None
        # ------------------------- return the actual function ------------------------
        return function(*args, **kw)

    # ------------------------------- return the wrapper ------------------------------
    return wrapper


def valid_time_dict(function):
    """A decorator function to check whether the time input is valid."""

    def wrapper(*args, **kw):

        if kw["time"]:
            if not {"hour", "minute", "second"} <= kw["time"].keys():
                return None
                # -------------------- return the actual function ---------------------
            return function(*args, **kw)
        # ------------------------- return the actual function ------------------------
        return function(*args, **kw)

    # ------------------------------- return the wrapper ------------------------------
    return wrapper


@valid_date_dict
@valid_time_dict
def from_dict_to_iso(
    date: Dict[Any, Any],
    time: Optional[Dict[Any, Any]],
    jalali: bool = True,
    timezone: bool = False,
    tzinfo: str = "Asia/Tehran",
) -> Optional[str]:
    """Coverts datetime dicts to ISO 8601 datetime string.

    Args:
        date (dict): The date value. Carefully choose the calendar. It is a
            required positional argument.
        time (dict): The
            time value. The default is datetime.time(0, 0, 0, 0).
        jalali (bool): if you use a dict of jalali dates, pass it True.
        timezone (bool): Adds the tzinfo to the end of SO 8601
            datetime string
        tzinfo (str): Specifies the timezone. Defaults to "Asia/Tehran".

    Returns:
        A text variable of <class 'str'> with ISO 8601 datetime standards.

    Examples:
    >>> date = {'month': 4, 'year': 1399, 'day': 31}
    >>> time = { 'hour': 15, 'minute': 38,'second': 6}
    >>> from_dict_to_iso(date, time, calendar='Jalali', timezone=True)
    '2020-07-21T15:38:06+03:26'
    """
    if time is None:
        time = {"hour": 0, "minute": 0, "second": 0}

    # ----------------------------- with timezone -----------------------------
    if jalali:
        result = from_jalali_dict_to_iso(
            date=date,
            time=time,
            timezone=timezone,
            tzinfo=tzinfo,
        )
    else:
        result = from_gregorian_dict_to_iso(
            date=date,
            time=time,
            timezone=timezone,
            tzinfo=tzinfo,
        )
    return result


def from_jalali_dict_to_iso(
    date: Dict[Any, Any],
    time: Mapping[Any, Any],
    timezone: bool = False,
    tzinfo: str = "Asia/Tehran",
) -> str:
    """Coverts jalali datetime dicts to ISO 8601 datetime string.

    Args:
        date (dict): The date value. Carefully choose the calendar. It is a
            required positional argument.
        time (dict): The
            time value. The default is datetime.time(0, 0, 0, 0).
        timezone (bool): Adds the tzinfo to the end of SO 8601
            datetime string
        tzinfo (str): Specifies the timezone. Defaults to "Asia/Tehran".

    Returns:
        A text variable of <class 'str'> with ISO 8601 datetime standards.

    Examples:
    >>> date = {'month': 4, 'year': 1399, 'day': 31}
    >>> time = { 'hour': 15, 'minute': 38,'second': 6}
    >>> from_jalali_dict_to_iso(date, time, timezone=True)
    '2020-07-21T15:38:06+03:26'
    """
    datetime_dict = {**date, **time}
    if timezone:
        datetime_object = (
            khayyam.JalaliDatetime(
                datetime_dict["year"],
                datetime_dict["month"],
                datetime_dict["day"],
                datetime_dict["hour"],
                datetime_dict["minute"],
                datetime_dict["second"],
                0,
            )
            .todatetime()
            .replace(tzinfo=pytz.timezone(tzinfo))
        )
    else:
        datetime_object = khayyam.JalaliDatetime(
            datetime_dict["year"],
            datetime_dict["month"],
            datetime_dict["day"],
            datetime_dict["hour"],
            datetime_dict["minute"],
            datetime_dict["second"],
            0,
        ).todatetime()
    result: str = datetime_object.isoformat()

    return result


def from_gregorian_dict_to_iso(
    date: Dict[Any, Any],
    time: Mapping[Any, Any],
    timezone: bool = False,
    tzinfo: str = "Asia/Tehran",
) -> str:
    """Coverts gregorian datetime dicts to ISO 8601 datetime string.

    Args:
        date (dict): The date value. Carefully choose the calendar. It is a
            required positional argument.
        time (dict): The
            time value. The default is datetime.time(0, 0, 0, 0).
        timezone (bool): Adds the tzinfo to the end of SO 8601 datetime string
        tzinfo (str): Specifies the timezone. Defaults to "Asia/Tehran".

    Returns:
        A text variable of <class 'str'> with ISO 8601 datetime standards.

    Examples:
    >>> date = {'month': 4, 'year': 2021, 'day': 12}
    >>> time = { 'hour': 15, 'minute': 38,'second': 6}
    >>> from_gregorian_dict_to_iso(date, time, timezone=True)
    '2021-04-12T15:38:06+03:26'
    """
    datetime_dict = {**date, **time}
    if timezone:
        datetime_object = datetime.datetime(
            datetime_dict["year"],
            datetime_dict["month"],
            datetime_dict["day"],
            datetime_dict["hour"],
            datetime_dict["minute"],
            datetime_dict["second"],
            0,
            tzinfo=pytz.timezone(tzinfo),
        )
    else:
        datetime_object = datetime.datetime(
            datetime_dict["year"],
            datetime_dict["month"],
            datetime_dict["day"],
            datetime_dict["hour"],
            datetime_dict["minute"],
            datetime_dict["second"],
            0,
        )
    result: str = datetime_object.isoformat()

    return result
