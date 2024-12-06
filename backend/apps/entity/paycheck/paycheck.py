from attr import attr
from attrs import define, field

from backend.apps.entity.income.income import Income, IncomeOrmModel
from backend.apps.entity.time.date_interval import DateInterval


@define
class Paycheck:
    income: Income = field(factory=Income)
    paycheck_income: float = attr(default=0.0)

    def __attrs_post_init__(self):
        self.paycheck_income = self.income_to_paycheck(self.income.income)

    @staticmethod
    def income_to_paycheck(income_value: float) -> float:
        bi_weeks_in_year: int = DateInterval.BI_WEEKLY.value
        return income_value / bi_weeks_in_year
