import unittest
from datetime import date

from backend.apps.models.date_utilities import get_next_bi_week, get_next_week
from backend.apps.entity.time.date_range import DateRange


class MyTestCase(unittest.TestCase):
    date_range = DateRange(date.today(), get_next_bi_week(date.today()))
    def test_in_range(self):
        start_next_week: date = get_next_week(date.today())
        self.assertTrue(self.date_range.in_range(start_next_week))


if __name__ == '__main__':
    unittest.main()
