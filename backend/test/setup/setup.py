from datetime import date

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.holding.saving.saving import Saving
from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome
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
        user_income_history=setup_income_history(),
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
    bonus: OneTimeIncome = OneTimeIncome(
        name="Bonus",
        amount=800,
        date_received=date.today()
    )
    payday: RecurringDate = RecurringDate(interval=YearInterval.BI_WEEKLY,
                                          day=get_next_friday_from_now())
    job: RecurringIncome = RecurringIncome(
        amount=1570,
        recurring_date=payday,
        name="Primary Job"
    )
    side_job: RecurringIncome = RecurringIncome(
        amount=210,
        recurring_date=payday,
        name="Second Job"
    )
    wage_job: WageIncome = WageIncome(
        name="Volunteer Stipend",
        amount=13,
        recurring_date=payday,
        weekly_hours=10
    )
    income_history: IncomeHistory = IncomeHistory()
    income_history.add_one_time_income(bonus)
    income_history.add_recurring_income(job)
    income_history.add_recurring_income(side_job)
    income_history.add_wage_income(wage_job)
    return income_history