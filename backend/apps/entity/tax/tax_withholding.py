from attrs import define


@define
class TaxWithholding:
    total_withheld: float = 0.0
    # TODO: Add list for tax withholding history

    def add_to_withholding(self, amount_withheld: float):
        self.total_withheld += amount_withheld