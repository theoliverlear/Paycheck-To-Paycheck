from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.time.due_date import DueDate

@define
class Bill(Identifiable):
    name: str = attr(default="")
    amount: float = attr(default=0.0)
    due_date: DueDate = attr(factory=DueDate)