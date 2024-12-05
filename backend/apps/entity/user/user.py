from attr import attr
from attrs import define

from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.user.safe_password import SafePassword


@define
class User:
    first_name: str = attr(default="")
    last_name: str = attr(default="")
    username: str = attr(default="")
    recurring_income: RecurringIncome = attr(factory=RecurringIncome)
    password: SafePassword = attr(factory=SafePassword)
