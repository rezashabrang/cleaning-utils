"""Makes a ISO 8601 datetime string from khayyam jalali datetime objects."""
# ------------------------ Import libraries and functions ---------------------
from typing import Optional

import khayyam
import pytz
from khayyam.jalali_datetime import JalaliDatetime as jdt

# ---------------------------- function definition ----------------------------


def from_khayyam_to_iso(
    date: khayyam.jalali_date.JalaliDate,
    time: Optional[
        khayyam.jalali_datetime.JalaliDatetime
    ] = khayyam.jalali_datetime.JalaliDatetime(hour=0, minute=0, second=0),
    jalali: bool = True,
    timezone: bool = False,
    tzinfo: str = "Asia/Tehran",
) -> str:
    """Coverts khayyam datetime objects to ISO 8601 datetime string.

    Args:
        date (khayyam.jalali_date.JalaliDate): The date value.
        time (khayyam.jalali_datetime.JalaliDatetime): The
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
        time = jdt(hour=0, minute=0, second=0)
    if timezone:
        datetime_object = (
            khayyam.JalaliDatetime.combine(date.todate(), time.todatetime().time())
            .todatetime()
            .replace(tzinfo=pytz.timezone(tzinfo))
        )
    # ---------------------------- without timezone ---------------------------
    else:
        datetime_object = khayyam.JalaliDatetime.combine(
            date.todate(),
            time.todatetime().time(),
        ).todatetime()

    result: str = datetime_object.isoformat()
    return result
