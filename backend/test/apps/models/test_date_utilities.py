import logging
import unittest
from datetime import date, timedelta

from backend.apps.models.date_utilities import get_next_year, get_next_bi_week
from backend.test.test_logging import log_test_class, log_test_results


@log_test_class(class_tested="date_utilities.py")
class DateUtilitiesTest(unittest.TestCase):
    @log_test_results
    def test_get_next_year(self):
        today: date = date.today()
        next_year: date = today.replace(year=today.year + 1)
        logging.info(f'Today: {today}')
        logging.info(f'Next Year: {next_year}')
        self.assertEqual(next_year, get_next_year(today))

    @log_test_results
    def test_get_next_bi_week(self):
        today: date = date.today()
        expected_next_bi_week: date = today + timedelta(weeks=2)
        actual_next_bi_week: date = get_next_bi_week(today)
        self.assertEqual(expected_next_bi_week, actual_next_bi_week)

if __name__ == '__main__':
    unittest.main()
