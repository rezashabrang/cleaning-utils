"""Makes a ISO 8601 datetime string."""
# ------------------------ Import libraries and functions ---------------------
from typing import Any, Dict, Optional, Union

import datetime

import khayyam

from cleaning_utils.from_datetime_to_iso import from_datetime_to_iso
from cleaning_utils.from_dict_to_iso import from_dict_to_iso
from cleaning_utils.from_khayyam_to_iso import from_khayyam_to_iso

# ---------------------------- function definition ----------------------------


def to_iso_datetime(
    date: Union[
        Dict[Any, Any],
        datetime.date,
        khayyam.jalali_date.JalaliDate,
    ],
    time: Optional[
        Union[
            Dict[Any, Any],
            datetime.time,
            khayyam.jalali_datetime.JalaliDatetime,
        ]
    ] = None,
    jalali: bool = True,
    timezone: bool = False,
    tzinfo: str = "Asia/Tehran",
) -> Any:
    """Coverts datetime objects to ISO 8601 datetime string.

    Args:
        date (dict or datetime.date, khayyam.jalali_date.JalaliDate): The date
            value. If you put a dict, carefully choose the calendar. It is a
            required positional argument.
        time (dict, datetime.time, khayyam.jalali_datetime.JalaliDatetime): The
            time value. The default is datetime.time(0, 0, 0, 0).
        jalali (bool): if you use a dict of jalali dates, pass it True.
        timezone (bool): Adds the tzinfo to the end of SO 8601 datetime string.
        tzinfo (str): Specifies the timezone. Defaults to "Asia/Tehran".

    Returns:
        A text variable of <class 'str'> with ISO 8601 datetime standards.

    Examples:
        >>> date = {
        ...         'month': 4,
        ...         'year': 1399,
        ...         'day': 31
        ...     }
        >>> time = {
        ...         'hour': 15,
        ...         'minute': 38,
        ...         'second': 6
        ...     }
        >>> to_iso_datetime(
        ...         date=date, time=time, jalali=True, timezone=True
        ...     )
        '2020-07-21T15:38:06+03:26'

    """
    # ------------------------- make true_date branch -------------------------
    converters = {
        dict: from_dict_to_iso,
        datetime.date: from_datetime_to_iso,
        khayyam.jalali_date.JalaliDate: from_khayyam_to_iso,
        str: none_returner,
    }
    result = converters[type(date)](
        date=date,
        time=time,
        jalali=jalali,
        timezone=timezone,
        tzinfo=tzinfo,
    )
    return result


def none_returner(
    date: Union[
        Dict[Any, Any],
        datetime.date,
        khayyam.jalali_date.JalaliDate,
    ],
    time: Optional[
        Union[
            Dict[Any, Any],
            datetime.time,
            khayyam.jalali_datetime.JalaliDatetime,
        ]
    ] = None,
    jalali: bool = True,
    timezone: bool = False,
    tzinfo: str = "Asia/Tehran",
) -> Any:
    """Returns None."""
    print(date, time, jalali, timezone, tzinfo)
