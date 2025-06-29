from datetime import date

from attr import attr
from attrs import define


@define
class WelcomeSurvey:
    last_paycheck_date: date = attr(default=date.today())
    paycheck_amount: float = attr(default=0.0)
    checking_account_amount: float = attr(default=0.0)