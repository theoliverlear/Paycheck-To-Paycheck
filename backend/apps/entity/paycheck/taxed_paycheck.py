from attr import attr
from attrs import define

from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.tax.tax import Tax


@define
class TaxedPaycheck(Paycheck):
    tax: Tax = attr(factory=Tax)
    after_tax_income: float = attr(default=0.0)
    deducted_from_paycheck: float = attr(default=0.0)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.deducted_from_paycheck = self.tax.amount_to_deduct(self.paycheck_income)
        self.after_tax_income = self.tax.amount_after_tax(self.paycheck_income)
