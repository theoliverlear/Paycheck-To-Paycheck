import logging
import unittest
from datetime import date

from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval
from backend.test.test_logging import log_test_class, log_test_results

def log_yearly_income_calculation(income_amount: float, interval: YearInterval.MONTHLY):
    calculated_yearly_total: float = income_amount * interval.value
    logging.info(f'Income is ${income_amount}, occuring {interval.value} times per year.')
    logging.info(f'The total should be when it should be ${calculated_yearly_total}.')

@log_test_class(class_tested="Recurring Income")
class RecurringIncomeTest(unittest.TestCase):
    recurring_income_test: RecurringIncome = RecurringIncome(income_amount=10,
                                                             recurring_date=RecurringDate(
                                                                 day=date.today(),
                                                                 interval=YearInterval.NO_INTERVAL
                                                             ))
    @log_test_results
    def test_calculate_yearly_income_daily(self):
        recurring_income = RecurringIncomeTest.recurring_income_test
        recurring_income.recurring_date.interval = YearInterval.DAILY
        year_interval = recurring_income.recurring_date.interval
        yearly_income = recurring_income.yearly_income
        income_amount = recurring_income.income_amount
        log_yearly_income_calculation(income_amount, year_interval)
        self.assertEqual(yearly_income, 3650.0)

    @log_test_results
    def test_calculate_yearly_income_monthly(self):
        recurring_income = RecurringIncomeTest.recurring_income_test
        recurring_income.recurring_date.interval = YearInterval.MONTHLY
        year_interval = recurring_income.recurring_date.interval
        yearly_income = recurring_income.yearly_income
        income_amount = recurring_income.income_amount
        log_yearly_income_calculation(income_amount, year_interval)
        self.assertEqual(yearly_income, 120.0)

if __name__ == '__main__':
    unittest.main()

