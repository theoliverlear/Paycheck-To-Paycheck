import unittest
from datetime import date

from backend.apps.models.date_utilities import get_next_bi_week, \
    get_next_week, get_next_month
from backend.apps.entity.time.date_range import DateRange


class MyTestCase(unittest.TestCase):
    date_range = DateRange(
        starting_date=date.today(),
        ending_date=get_next_bi_week(date.today())
    )
    def test_in_range(self):
        today: date = date.today()
        start_next_week: date = get_next_week(today)
        in_range: bool = self.date_range.in_range(start_next_week)
        self.date_range.print_in_range(start_next_week)
        self.assertTrue(in_range)

        next_month: date = get_next_month(today)
        in_range = self.date_range.in_range(next_month)
        self.date_range.print_in_range(next_month)
        self.assertFalse(in_range)



if __name__ == '__main__':
    unittest.main()
