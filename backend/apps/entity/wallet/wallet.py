from abc import ABC
from typing import override

from attr import attr
from attrs import define

from backend.apps.entity.bill.undated_bill import UndatedBill
from backend.apps.entity.holding.debt.debt import Debt
from backend.apps.entity.holding.saving.saving import Saving
from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.undated_income import UndatedIncome
from backend.apps.entity.orm_compatible import OrmCompatible, M, O
from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.wallet.models import WalletOrmModel
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class Wallet(Identifiable, OrmCompatible['Wallet', WalletOrmModel], ABC):
    checking_account: Saving = attr(factory=Saving)
    savings: list[Saving] = attr(default=[])
    debts: list[Debt] = attr(default=[])

    def process_bill(self, bill: UndatedBill):
        self.checking_account -= bill.amount

    def process_income(self, income: UndatedIncome):
        self.checking_account += income.amount

    def process_paycheck(self, paycheck: Paycheck):
        self.checking_account += paycheck.total_income - paycheck.total_bills

    @override
    def save(self) -> 'Wallet':
        if self.is_initialized():
            self.update()
            return self
        else:
            pass

    @override
    def update(self) -> None:
        try:
            pass
        except WalletOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    @override
    def set_from_orm_model(self, orm_model: WalletOrmModel) -> None:
        self.id = orm_model.id
        self.checking_account = Saving.from_orm_model(orm_model.checking_account)
        # TODO: Use a service to get all savings.
        # TODO: Use a service to get all debts.


    @override
    def get_orm_model(self) -> WalletOrmModel:
        return WalletOrmModel(
            id=self.id
        )

    @staticmethod
    @override
    def set_orm_model(db_model: WalletOrmModel, model_to_match: WalletOrmModel) -> None:
        db_model.id = model_to_match.id
        db_model.checking_account = model_to_match.checking_account

    @staticmethod
    @override
    def from_orm_model(orm_model: WalletOrmModel) -> 'Wallet':
        wallet: Wallet = Wallet()
        wallet.set_from_orm_model(orm_model)
        return wallet

