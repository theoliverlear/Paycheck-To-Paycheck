from abc import ABC
from typing import override, TYPE_CHECKING

from attr import attr
from attrs import define

from backend.apps.entity.bill.undated_bill import UndatedBill
if TYPE_CHECKING:
    from backend.apps.entity.holding.debt.debt import Debt
    from backend.apps.entity.holding.saving.saving import Saving
from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.undated_income import UndatedIncome
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.wallet.models import WalletOrmModel
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class Wallet(Identifiable, OrmCompatible['Wallet', WalletOrmModel], ABC):
    checking_account: 'Saving' = attr(default=None)
    savings: list['Saving'] = attr(default=[])
    debts: list['Debt'] = attr(default=[])

    def process_bill(self, bill: UndatedBill):
        self.checking_account -= bill.amount

    def process_income(self, income: UndatedIncome):
        self.checking_account += income.amount

    def process_paycheck(self, paycheck: Paycheck):
        self.checking_account += paycheck.total_income - paycheck.total_bills


    def add_wallet_to_dependencies(self):
        self.checking_account.wallet = self
        for saving in self.savings:
            saving.wallet = self
        for debt in self.debts:
            debt.wallet = self

    @override
    def save(self) -> 'Wallet':
        if self.is_initialized():
            self.update()
            return self
        else:
            saved_wallet: WalletOrmModel = WalletOrmModel.objects.create()
            self.set_from_orm_model(saved_wallet)
            return Wallet.from_orm_model(saved_wallet)


    def save_all(self) -> 'Wallet':
        if self.is_initialized():
            self.update_all()
        else:
            saved_wallet: WalletOrmModel = WalletOrmModel.objects.create()
            self.set_from_orm_model(saved_wallet)
            self.save_checking()
            self.save_all_savings()
            self.save_all_debts()
            return Wallet.from_orm_model(saved_wallet)


    def save_checking(self) -> 'Saving':
        checking_account: Saving = self.checking_account.save()
        self.checking_account = checking_account
        return checking_account

    def save_all_savings(self) -> list['Saving']:
        saved_savings: list['Saving'] = []
        for saving in self.savings:
            saved_saving: Saving = saving.save()
            saved_savings.append(saved_saving)
        self.savings = saved_savings
        return saved_savings

    def save_all_debts(self) -> list['Debt']:
        saved_debts: list['Debt'] = []
        for debt in self.debts:
            saved_debt: Debt = debt.save()
        self.debts = saved_debt
        return saved_debts

    @override
    def update(self) -> None:
        try:
            db_model: WalletOrmModel = WalletOrmModel.objects.get(id=self.id)
            orm_model: WalletOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except WalletOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    def update_all(self) -> None:
        try:
            db_model: WalletOrmModel = WalletOrmModel.objects.get(id=self.id)
            self.update_checking()
            self.update_all_savings()
            self.save_all_debts()
            orm_model: WalletOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except WalletOrmModel.DoesNotExist as exception:
            raise EntityNotFoundException(self)

    def update_checking(self):
        self.checking_account.update()

    def update_all_savings(self):
        for saving in self.savings:
            saving.update()

    def update_all_debts(self):
        for debt in self.debts:
            debt.update()

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