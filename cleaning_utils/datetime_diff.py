"""Finding the time differences between two timestamps or datetime objects."""
# ------------------------ Import libraries and functions ---------------------
import datetime
import re

import dateutil.parser

from cleaning_utils.constants import DATE_SET, ISO_PATTERN, TIME_SET

# ---------------------------- function definition ----------------------------


def datetime_diff(dt1, dt2):
    """Calculates the differences between two timestamps or datetime objects.

    Args:
        dt1 (dict or ISO 8601 str):
            The first datetime input
        dt2 (dict or ISO 8601 str):
            The second datetime input

    Returns:
        A <class 'datetime.timedelta'> from dt2 - dt1.

    Raises:
        Exception: If the input is not a known ISO 8601.

    Examples:
        >>> datetime1 = {
        ...         'month': 1,
        ...         'year': 1399,
        ...         'day': 4,
        ...         'hour': 23,
        ...         'minute': 5,
        ...         'second': 25
        ...     }
        >>> datetime2 = {
        ...         'month': 1,
        ...         'year': 1399,
        ...         'day': 8,
        ...         'hour': 0,
        ...         'minute': 1,
        ...         'second': 0
        ...     }
        >>> datetime_diff(datetime1, datetime2)
        datetime.timedelta(days=3, seconds=3335)
        >>> datetime3 = '2020-03-23T23:05:25+03:26'
        >>> datetime4 = '2020-03-27T00:01:00+03:26'
        >>> datetime_diff(datetime3, datetime4)
        datetime.timedelta(days=3, seconds=3335)

    """
    # -------------------------- string input branch --------------------------
    # string pattern for checking whether the input is a known ISO 8601
    if isinstance(dt2, str) and isinstance(dt1, str):
        if bool(re.match(re.compile(ISO_PATTERN), dt1)) and bool(
            re.match(re.compile(ISO_PATTERN), dt2),
        ):
            result = dateutil.parser.parse(dt2) - dateutil.parser.parse(dt1)
        else:
            raise Exception("unknown datetime formats")
    # --------------------------- dict input branch ---------------------------
    elif isinstance(dt2, dict) and isinstance(dt1, dict):
        if len(dt1.keys()) == len(dt2.keys()) == 6:
            if (TIME_SET <= dt1.keys()) and (TIME_SET <= dt2.keys()):
                result = datetime.datetime(
                    dt2["year"],
                    dt2["month"],
                    dt2["day"],
                    dt2["hour"],
                    dt2["minute"],
                    dt2["second"],
                ) - datetime.datetime(
                    dt1["year"],
                    dt1["month"],
                    dt1["day"],
                    dt1["hour"],
                    dt1["minute"],
                    dt1["second"],
                )
            else:
                raise Exception("unknown datetime formats")
        elif len(dt1.keys()) == len(dt2.keys()) == 3:
            if (DATE_SET <= dt1.keys()) and (DATE_SET <= dt2.keys()):
                result = (
                    datetime.datetime(
                        dt2["year"],
                        dt2["month"],
                        dt2["day"],
                    )
                    - datetime.datetime(dt1["year"], dt1["month"], dt1["day"])
                )
            else:
                raise Exception("unknown datetime formats")
        else:
            raise Exception("unknown datetime formats")
    # ------------------------- incorrect input branch ------------------------
    else:
        raise Exception("unknown datetime formats")
    return result
