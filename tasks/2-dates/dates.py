from datetime import datetime, date
from typing import List

from constants import date_1, date_2, string_date


def get_seconds_between_datetimes(start_date: datetime, end_date: datetime) -> int:
    """This method should calculate the number of seconds between two datetimes."""

    output = 0  # Replace with your logic

    return output


def parse_unusual_date_string(date_string: str) -> date:
    """This method should parse a string into a `date` object.

    Note: The `string_date` value is in a very strange format. This method only
    needs to work for that format.
    """

    output = date.today()  # Replace with your logic

    return output


def add_eight_days_to_date(start_date: datetime) -> datetime:
    """This method should add eight days to the `start_date`."""

    output = start_date  # Replace with your logic

    return output


def set_to_end_of_day(start_date: datetime) -> datetime:
    """This method should set a datetime to the end of the day, i.e. just before midnight."""

    output = start_date  # Replace with your logic

    return output


# These results are checked by the test. Don't modify this.
time_between_datetimes = get_seconds_between_datetimes(date_1, date_2)
parsed_unusual_date = parse_unusual_date_string(string_date)
add_eight_days = add_eight_days_to_date(date_1)
end_of_day = set_to_end_of_day(date_2)
