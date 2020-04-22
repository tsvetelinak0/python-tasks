import unittest
from datetime import date, datetime, timedelta

from dates import time_between_datetimes, parsed_unusual_date, add_eight_days, end_of_day


class TestDates(unittest.TestCase):

    def test__seconds_between_datetimes(self):
        """Assert that the number of seconds between the two dates is calculated correctly."""

        result = time_between_datetimes
        expected = 14782233

        self.assertEqual(result, expected)


    def test__unusual_date_parsing(self):
        """Assert that string date is parsed correctly."""

        result = parsed_unusual_date
        expected = date(2019, 3, 27)

        self.assertEqual(result, expected)


    def test__add_eight_days(self):
        """Assert eight days are added to the date correctly."""

        result = add_eight_days
        expected = datetime(2019, 7, 31, 11, 47, 3)

        self.assertEqual(result, expected)


    def test__end_of_day(self):
        """Assert datetime is set to end of day correctly."""

        result = end_of_day
        expected = datetime(2020, 1, 10, 23, 59, 59, 999999)

        self.assertEqual(result, expected)
