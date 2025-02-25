from attr import attr
from attrs import define, field

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.time.year_interval import YearInterval


@define
class Paycheck(Identifiable):
    income: RecurringIncome = field(factory=RecurringIncome)
    paycheck_income: float = attr(default=0.0)

    def __attrs_post_init__(self):
        self.paycheck_income = self.income_to_paycheck(self.income.income_amount)

    @staticmethod
    def income_to_paycheck(income_value: float) -> float:
        bi_weeks_in_year: int = YearInterval.BI_WEEKLY.value
        return income_value / bi_weeks_in_year
