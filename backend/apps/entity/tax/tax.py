from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable


@define
class Tax(Identifiable):
    rate: float = attr(default=0.0)

    def amount_after_tax(self, amount: float):
        return amount - self.amount_to_deduct(amount)

    def amount_to_deduct(self, amount: float):
        tax_amount = amount * self.rate_as_decimal()
        return tax_amount

    def rate_as_decimal(self):
        return self.rate / 100
