import unittest
from datetime import date

from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.user.user import User
from backend.apps.models.date_utilities import get_next_friday
from backend.test.apps.entity.user.test_user import setup_user, \
    recurring_income
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

@log_test_class(class_tested="Paycheck")
class PaycheckTest(unittest.TestCase):
    income_history_test: IncomeHistory = setup_income_history()
    user_test: User = setup_user()
    paycheck_test: Paycheck = Paycheck()

    @classmethod
    def setUpClass(cls):
        PaycheckTest.user_test.user_income_history = PaycheckTest.income_history_test
        PaycheckTest.paycheck_test = Paycheck(
            one_time_incomes=PaycheckTest.income_history_test.one_time_incomes,
            recurring_incomes=PaycheckTest.income_history_test.recurring_incomes,
            wage_incomes=PaycheckTest.income_history_test.wage_incomes
        )

    @log_test_results
    def test_total_income(self):
        wage_income: float = 260
        job_income: float = 1570
        side_job_income: float = 210
        one_time_income: float = 800
        expected_total: float = wage_income + job_income + side_job_income + one_time_income
        PaycheckTest.paycheck_test.print_all_incomes()
        self.assertEqual(expected_total, PaycheckTest.paycheck_test.get_total_income())

if __name__ == '__main__':
    unittest.main()