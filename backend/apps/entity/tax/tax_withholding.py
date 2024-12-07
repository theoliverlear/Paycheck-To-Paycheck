from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable


@define
class TaxWithholding(Identifiable):
    total_withheld: float = attr(default=0.0)
    # TODO: Add list for tax withholding history

    def add_to_withholding(self, amount_withheld: float):
        self.total_withheld += amount_withheld