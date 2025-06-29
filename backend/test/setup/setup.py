# setup.py
import copy
import logging
from datetime import date

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.holding.saving.saving import Saving
from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.entity.user.user import User
from backend.apps.entity.wallet.wallet import Wallet
from backend.apps.models.date_utilities import get_next_friday_from_now


def setup_user() -> User:
    safe_password: SafePassword = SafePassword(unhashed_password='password')
    user: User = User(
        first_name='John',
        last_name='Doe',
        username='johndoe',
        password=safe_password,
        user_income_history=copy.deepcopy(setup_income_history()),
        user_bill_history=BillHistory(),
        wallet=setup_wallet(),
        payday=RecurringDate(day=date(day=4, month=4, year=2025), interval=YearInterval.BI_WEEKLY)
    )
    return user

def setup_wallet() -> Wallet:
    checking_account: Saving = Saving(
        name="Checking Account",
        amount=1000
    )
    return Wallet(checking_account=checking_account)

def setup_income_history() -> IncomeHistory:
    income_history: IncomeHistory = copy.deepcopy(IncomeHistory())
    bonus: OneTimeIncome = copy.deepcopy(OneTimeIncome(
        name="Bonus",
        amount=800,
        date_received=date.today(),
        income_history=income_history
    ))
    payday: RecurringDate = copy.deepcopy(RecurringDate(interval=YearInterval.BI_WEEKLY,
                                          day=get_next_friday_from_now()))
    job: RecurringIncome = copy.deepcopy(RecurringIncome(
        amount=1570,
        recurring_date=payday,
        name="Primary Job",
        income_history=income_history
    ))
    side_job: RecurringIncome = copy.deepcopy(RecurringIncome(
        amount=210,
        recurring_date=payday,
        name="Second Job",
        income_history=income_history
    ))
    wage_job: WageIncome = copy.deepcopy(WageIncome(
        name="Volunteer Stipend",
        amount=13,
        recurring_date=payday,
        weekly_hours=10,
        income_history=income_history
    ))
    income_history.add_one_time_income(bonus)
    income_history.add_recurring_income(job)
    income_history.add_recurring_income(side_job)
    income_history.add_wage_income(wage_job)
    return income_history

def get_test_paycheck():
    income_history = copy.deepcopy(setup_income_history())
    user = copy.deepcopy(setup_user())
    user.user_income_history = income_history
    # return Paycheck(
    #     one_time_incomes=income_history.one_time_incomes,
    #     recurring_incomes=income_history.recurring_incomes,
    #     wage_incomes=income_history.wage_incomes
    # )
    paycheck: Paycheck = copy.deepcopy(Paycheck.from_user(user, date.today()))
    logging.info('~' * 50)
    paycheck.print_all_incomes()
    logging.info('~' * 50)
    return copy.deepcopy(paycheck)

def get_test_one_time_income() -> OneTimeIncome:
    test_one_time_income: OneTimeIncome = OneTimeIncome(
        name="Test One Time Income", amount=1000.00,
        date_received=date.today())
    return copy.deepcopy(test_one_time_income)

def get_test_recurring_income() -> RecurringIncome:
    test_recurring_income: RecurringIncome = RecurringIncome(
        name="Test Recurring Income", amount=500.00,
        recurring_date=RecurringDate(
            interval=YearInterval.BI_WEEKLY,
            day=date.today()))
    return copy.deepcopy(test_recurring_income)

def get_test_wage_income() -> WageIncome:
    test_wage_income: WageIncome = WageIncome(
        name="Test Wage Income", amount=20.00,
        recurring_date=RecurringDate(
            interval=YearInterval.BI_WEEKLY,
            day=date.today()), weekly_hours=10)
    return copy.deepcopy(test_wage_income)