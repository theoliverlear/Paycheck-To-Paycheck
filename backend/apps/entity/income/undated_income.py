from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable

@define
class UndatedIncome(Identifiable):
    name: str = attr(default="")
    _income_amount: float = attr(default=0.0)

    @property
    def income_amount(self):
        return self._income_amount

    @income_amount.setter
    def income_amount(self, income_amount):
        self._income_amount = income_amount