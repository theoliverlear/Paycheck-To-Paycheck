from attr import attr
from attrs import define

from backend.apps.entity.income.income import Income
from backend.apps.entity.time.recurring_date import RecurringDate

@define
class RecurringIncome:
    recurring_date: RecurringDate = attr(factory=RecurringDate)
    income: Income = attr(factory=Income)