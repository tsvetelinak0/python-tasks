import unittest

from duplicates import deduped_list, list_of_duplicates


class TestDuplicates(unittest.TestCase):

    def test__remove_duplicates(self):
        """Assert that duplicates are removed."""

        result = deduped_list
        expected = [
            'Fred',
            'Dave',
            'Sarah',
            'John',
            'Matthew',
            'Joanna',
            'Marjorie',
            'Anna',
            'Tony',
            'Sam',
            'Eric',
            'Susan',
            'Arthur',
        ]

        self.assertListEqual(sorted(result), sorted(expected))


    def test__get_duplicates(self):
        """Assert that duplicates are listed."""

        result = list_of_duplicates
        expected = [
            'Fred',
            'Sarah',
            'Matthew',
            'Joanna',
            'Sam',
        ]

        self.assertListEqual(sorted(result), sorted(expected))

