"""Makes a ISO 8601 datetime string from datetime objects."""
# ------------------------ Import libraries and functions ---------------------
from typing import Optional

import datetime

import pytz

# ---------------------------- function definition ----------------------------


def from_datetime_to_iso(
    date: datetime.date,
    time: Optional[datetime.time] = datetime.time(0, 0, 0, 0),
    jalali: bool = False,
    timezone: bool = False,
    tzinfo: str = "Asia/Tehran",
) -> str:
    """Coverts datetime objects to ISO 8601 datetime string.

    Args:
        date (datetime.date): The date
            value. It is a required positional argument.
        time (datetime.time): The
            time value. The default is datetime.time(0, 0, 0, 0).
        jalali (bool): if you use a dict of jalali dates, pass it True.
        timezone (bool): Adds the tzinfo to the end of SO 8601
            datetime string
        tzinfo (str): Specifies the timezone. Defaults to "Asia/Tehran".

    Returns:
        A text variable of <class 'str'> with ISO 8601 datetime standards.

    """
    # ----------------------------- with timezone -----------------------------
    print(jalali)
    if time is None:
        time = datetime.time(0, 0, 0, 0)

    if timezone:
        datetime_object = datetime.datetime.combine(
            date,
            time,
            tzinfo=pytz.timezone(tzinfo),
        )
    # ---------------------------- without timezone ---------------------------
    else:
        datetime_object = datetime.datetime.combine(date, time)

    result: str = datetime_object.isoformat()
    return result
