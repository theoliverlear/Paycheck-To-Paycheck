from attr import attr
from attrs import define

from backend.apps.entity.time.recurring_date import RecurringDate

@define
class RecurringBill:
    name: str = attr(default="")
    amount: float = attr(default=0.0)
    recurring_date: RecurringDate = attr(factory=RecurringDate)