from attr import attr
from attrs import define, field

from backend.apps.entity.income.income import Income

@define
class Paycheck:
    income: Income = field(factory=Income)
    paycheck_income: float = attr(default=0.0)

    def __attrs_post_init__(self):
        self.paycheck_income = self.income_to_paycheck(self.income.income)

    @staticmethod
    def income_to_paycheck(income_value: float) -> float:
        BIWEEKLY_PAY_PERIODS: int = 26
        return income_value / BIWEEKLY_PAY_PERIODS
