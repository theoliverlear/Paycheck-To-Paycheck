from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable

@define
class UndatedBill(Identifiable):
    name: str = attr(default="")
    amount: float = attr(default=0.0)