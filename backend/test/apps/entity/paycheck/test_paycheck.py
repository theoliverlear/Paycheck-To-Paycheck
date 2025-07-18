# test_paycheck.py
import logging
import unittest
from datetime import date

from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.bill.recurring_bill import RecurringBill
from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.time.date_range import DateRange
from backend.apps.entity.time.due_date import DueDate
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.models.date_utilities import get_next_friday_from_now, \
    get_next_bi_week, get_next_month, get_next_week, get_next_year, \
    get_tomorrow
from backend.test.apps.entity.user.test_user import setup_user
from backend.test.setup.setup import get_test_paycheck, setup_income_history, \
    get_test_one_time_income, get_test_recurring_income
from backend.test.test_logging import log_test_class, log_test_results

@log_test_class(class_tested="Paycheck")
class PaycheckTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.test_paycheck = get_test_paycheck()
        logging.info(f'Setup paycheck ID: {id(self.test_paycheck)}')

    @log_test_results
    def test_total_income(self):
        paycheck: Paycheck = get_test_paycheck()
        wage_income: float = 260
        job_income: float = 1570
        side_job_income: float = 210
        one_time_income: float = 800
        expected_total: float = wage_income + job_income + side_job_income + one_time_income
        paycheck.print_all_incomes()
        paycheck.remove_one_time_income("Birthday Present")
        self.assertEqual(expected_total, paycheck.get_total_income())

    @log_test_results
    def test_date_range_increase(self):
        paycheck: Paycheck = get_test_paycheck()
        original_date_range: DateRange = DateRange(start_date=date.today(),
                                                   end_date=get_next_bi_week(date.today()))
        paycheck.date_range.start_date = get_next_bi_week(paycheck.date_range.start_date)
        paycheck.date_range.end_date = get_next_bi_week(paycheck.date_range.end_date)
        self.assertNotEqual(original_date_range, paycheck.date_range)

    @log_test_results
    def test_purge_outdated_items(self):
        paycheck: Paycheck = get_test_paycheck()
        # paycheck.date_range.start_date = date.today()
        # paycheck.date_range.end_date = get_next_bi_week(date.today())
        paycheck.add_one_time_bill(OneTimeBill(
            due_date=DueDate(due_date=get_next_month(date.today())),
            name="Tires",
            amount=650.5
        ))
        paycheck.add_recurring_bill(RecurringBill(
            amount=250.1,
            name="Car Payment",
            recurring_date=RecurringDate(day=get_next_week(date.today()),
                                         interval=YearInterval.MONTHLY),
        ))
        paycheck.add_one_time_income(OneTimeIncome(
            name="Birthday Present",
            date_received=get_tomorrow(date.today()),
            amount=50
        ))
        paycheck.add_recurring_income(RecurringIncome(
            name="Stock Dividends",
            amount=60,
            recurring_date=RecurringDate(day=get_next_year(date.today()),
                                         interval=YearInterval.MONTHLY)
        ))
        paycheck.add_wage_income(WageIncome(
            recurring_date=RecurringDate(day=date.today(),
                                         interval=YearInterval.BI_WEEKLY),
            amount=14.25,
            name="Third Job",
            weekly_hours=40,
        ))
        num_incomes: int = paycheck.get_num_incomes()
        num_bills: int = paycheck.get_num_bills()
        expected_incomes: int = 6
        expected_bills: int = 1
        paycheck.print_all_incomes()
        logging.info("-" * 50)
        # for income in setup_income_history().recurring_incomes:
            # logging.info(f"Recurring Income: {income}")
        self.assertEqual(num_incomes, expected_incomes)
        self.assertEqual(num_bills, expected_bills)


    @log_test_results
    def test_add_one_time_income(self):
        paycheck: Paycheck = get_test_paycheck()
        income_history: IncomeHistory = IncomeHistory()
        test_one_time_income: OneTimeIncome = get_test_one_time_income()
        test_one_time_income.income_history = income_history
        paycheck.add_one_time_income(test_one_time_income)
        paycheck.add_one_time_income(test_one_time_income)
        paycheck.add_one_time_income(test_one_time_income)
        self.assertEqual(len(paycheck.one_time_incomes), 2)

    @log_test_results
    def test_add_recurring_income(self):
        logging.info('=' * 50)
        self.test_paycheck.print_all_incomes()
        logging.info('=' * 50)
        income_history: IncomeHistory = IncomeHistory()
        test_recurring_income: RecurringIncome = get_test_recurring_income()
        test_recurring_income.income_history = income_history
        self.assertEqual(len(self.test_paycheck.recurring_incomes), 2)
        self.test_paycheck.add_recurring_income(test_recurring_income)
        self.test_paycheck.add_recurring_income(test_recurring_income)
        self.assertEqual(len(self.test_paycheck.recurring_incomes), 3)

    @log_test_results
    def test_paycheck_date_differences(self):
        base_paycheck: Paycheck = get_test_paycheck()
        test_paycheck: Paycheck = get_test_paycheck()
        test_paycheck.date_range = DateRange.get_paycheck_range(get_next_year(date.today()))
        # logging.info(f'Base paycheck: {base_paycheck}')
        # logging.info(f'Test paycheck: {test_paycheck}')
        self.assertNotEqual(base_paycheck, test_paycheck)

if __name__ == '__main__':
    unittest.main()