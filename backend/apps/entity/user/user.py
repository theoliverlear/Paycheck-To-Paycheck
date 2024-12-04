from attr import attr
from attrs import define

from backend.apps.entity.income.income import Income
from backend.apps.entity.user.safe_password import SafePassword


@define
class User:
    first_name: str = attr(default="")
    last_name: str = attr(default="")
    username: str = attr(default="")
    income: Income = attr(default=Income())
    password: SafePassword = attr(default=SafePassword())