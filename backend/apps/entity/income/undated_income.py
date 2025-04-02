from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable

@define
class UndatedIncome(Identifiable):
    name: str = attr(default="")
    _amount: float = attr(default=0.0)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount