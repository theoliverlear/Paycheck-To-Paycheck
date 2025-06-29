import unittest
from datetime import date

from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.test.test_logging import log_test_class, log_test_results
from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.time.year_interval import YearInterval


@log_test_class(class_tested="IncomeHistory")
class IncomeHistoryTest(unittest.TestCase):
    @log_test_results
    def test_add_one_time_income(self):
        income_history: IncomeHistory = IncomeHistory()
        test_one_time_income: OneTimeIncome = OneTimeIncome(income_history=income_history,
                                                            name="Test One Time Income", amount=1000.00,
                                                            date_received=date.today())
        income_history.add_one_time_income(test_one_time_income)
        income_history.add_one_time_income(test_one_time_income)
        self.assertEqual(len(income_history.one_time_incomes), 1)

    @log_test_results
    def test_adding_recurring_income(self):
        income_history: IncomeHistory = IncomeHistory()
        test_recurring_income: RecurringIncome = RecurringIncome(income_history=income_history,
                                                                 name="Test Recurring Income", amount=500.00,
                                                                 recurring_date=RecurringDate(
                                                                     interval=YearInterval.BI_WEEKLY,
                                                                     day=date.today()))
        income_history.add_recurring_income(test_recurring_income)
        income_history.add_recurring_income(test_recurring_income)
        self.assertEqual(len(income_history.recurring_incomes), 1)

    @log_test_results
    def test_adding_wage_income(self):
        income_history: IncomeHistory = IncomeHistory()
        from backend.apps.entity.time.year_interval import YearInterval
        test_wage_income: WageIncome = WageIncome(income_history=income_history,
                                                  name="Test Wage Income", amount=20.00,
                                                  recurring_date=RecurringDate(
                                                      interval=YearInterval.BI_WEEKLY,
                                                      day=date.today()), weekly_hours=10)
        income_history.add_wage_income(test_wage_income)
        income_history.add_wage_income(test_wage_income)
        self.assertEqual(len(income_history.wage_incomes), 1)
if __name__ == '__main__':
    unittest.main()
