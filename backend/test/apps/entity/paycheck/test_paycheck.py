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
from backend.apps.entity.user.user import User
from backend.apps.models.date_utilities import get_next_friday, \
    get_next_bi_week, get_next_month, get_next_week, get_next_year, \
    get_tomorrow
from backend.test.apps.entity.user.test_user import setup_user
from backend.test.test_logging import log_test_class, log_test_results


def setup_income_history() -> IncomeHistory:
    bonus: OneTimeIncome = OneTimeIncome(
        name="Bonus",
        income_amount=800,
        date_received=date.today()
    )
    payday: RecurringDate = RecurringDate(interval=YearInterval.BI_WEEKLY,
                                   day=get_next_friday())
    job: RecurringIncome = RecurringIncome(
        income_amount=1570,
        recurring_date=payday,
        name="Primary Job"
    )
    side_job: RecurringIncome = RecurringIncome(
        income_amount=210,
        recurring_date=payday,
        name="Second Job"
    )
    wage_job: WageIncome = WageIncome(
        name="Volunteer Stipend",
        income_amount=13,
        recurring_date=payday,
        weekly_hours=10
    )
    income_history: IncomeHistory = IncomeHistory()
    income_history.add_one_time_income(bonus)
    income_history.add_recurring_income(job)
    income_history.add_recurring_income(side_job)
    income_history.add_wage_income(wage_job)
    return income_history

def get_test_paycheck():
    income_history = setup_income_history()
    user = setup_user()
    user.user_income_history = income_history
    return Paycheck(
        one_time_incomes=income_history.one_time_incomes,
        recurring_incomes=income_history.recurring_incomes,
        wage_incomes=income_history.wage_incomes
    )

@log_test_class(class_tested="Paycheck")
class PaycheckTest(unittest.TestCase):
    # income_history_test: IncomeHistory = setup_income_history()
    # user_test: User = setup_user()
    # paycheck_test: Paycheck = Paycheck()

    # def setUp(self):
    #     PaycheckTest.income_history_test = IncomeHistory()
    #     PaycheckTest.income_history_test = setup_income_history()
    #     PaycheckTest.user_test = User()
    #     PaycheckTest.user_test = setup_user()
    #     PaycheckTest.user_test.user_income_history = PaycheckTest.income_history_test
    #     PaycheckTest.paycheck_test = Paycheck(
    #     one_time_incomes=PaycheckTest.income_history_test.one_time_incomes,
    #     recurring_incomes=PaycheckTest.income_history_test.recurring_incomes,
    #     wage_incomes=PaycheckTest.income_history_test.wage_incomes
    # )
    #
    # @classmethod
    # def setUpClass(cls):
    #     PaycheckTest.user_test.user_income_history = PaycheckTest.income_history_test
    #     PaycheckTest.paycheck_test = Paycheck(
    #         one_time_incomes=PaycheckTest.income_history_test.one_time_incomes,
    #         recurring_incomes=PaycheckTest.income_history_test.recurring_incomes,
    #         wage_incomes=PaycheckTest.income_history_test.wage_incomes
    #     )

    @log_test_results
    def test_total_income(self):
        income_history = setup_income_history()
        user = setup_user()
        user.user_income_history = income_history
        paycheck: Paycheck = Paycheck(
            one_time_incomes=income_history.one_time_incomes,
            recurring_incomes=income_history.recurring_incomes,
            wage_incomes=income_history.wage_incomes
        )
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
        income_history = setup_income_history()
        user = setup_user()
        user.user_income_history = income_history
        paycheck: Paycheck = Paycheck(
            one_time_incomes=income_history.one_time_incomes,
            recurring_incomes=income_history.recurring_incomes,
            wage_incomes=income_history.wage_incomes
        )
        original_date_range: DateRange = DateRange(starting_date=date.today(),
                                                   ending_date=get_next_bi_week(date.today()))
        paycheck.date_range.starting_date = get_next_bi_week(paycheck.date_range.starting_date)
        paycheck.date_range.ending_date = get_next_bi_week(paycheck.date_range.ending_date)
        self.assertNotEqual(original_date_range, paycheck.date_range)

    @log_test_results
    def test_purge_outdated_items(self):
        income_history = setup_income_history()
        user = setup_user()
        user.user_income_history = income_history
        paycheck: Paycheck = Paycheck(
            one_time_incomes=income_history.one_time_incomes,
            recurring_incomes=income_history.recurring_incomes,
            wage_incomes=income_history.wage_incomes
        )
        paycheck.date_range.starting_date = date.today()
        paycheck.date_range.ending_date = get_next_bi_week(date.today())
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
            income_amount=50
        ))
        paycheck.add_recurring_income(RecurringIncome(
            name="Stock Dividends",
            income_amount=60,
            recurring_date=RecurringDate(day=get_next_year(date.today()),
                                         interval=YearInterval.MONTHLY)
        ))
        paycheck.add_wage_income(WageIncome(
            recurring_date=RecurringDate(day=date.today(),
                                         interval=YearInterval.BI_WEEKLY),
            income_amount=14.25,
            name="Third Job",
            weekly_hours=40,
        ))
        num_incomes: int = paycheck.get_num_incomes()
        num_bills: int = paycheck.get_num_bills()
        expected_incomes: int = 6
        expected_bills: int = 1
        income_history = setup_income_history()
        user = setup_user()
        user.user_income_history = income_history
        paycheck = Paycheck(
            one_time_incomes=income_history.one_time_incomes,
            recurring_incomes=income_history.recurring_incomes,
            wage_incomes=income_history.wage_incomes
        )
        self.assertEqual(num_incomes, expected_incomes)
        self.assertEqual(num_bills, expected_bills)

if __name__ == '__main__':
    unittest.main()