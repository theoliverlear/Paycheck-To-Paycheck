from attr import attr
from attrs import define

from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome


@define
class IncomesResponse:
    one_time_incomes: list[OneTimeIncome] = attr(default=[])
    recurring_incomes: list[RecurringIncome] = attr(default=[])
    wage_incomes: list[WageIncome] = attr(default=[])