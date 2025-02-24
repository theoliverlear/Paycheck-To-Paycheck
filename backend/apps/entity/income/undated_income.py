from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable

@define
class UndatedIncome(Identifiable):
    name: str = attr(default="")
    income_amount: float = attr(default=0.0)
