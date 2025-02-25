from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

from attr import attr
from attrs import define

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.identifiable import Identifiable
from backend.resolve_class import resolve_class

if TYPE_CHECKING:
    from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.user.models import UserOrmModel
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class User(OrmCompatible['User', UserOrmModel], ABC, Identifiable):
    first_name: str = attr(default="")
    last_name: str = attr(default="")
    email: str = attr(default="")
    username: str = attr(default="")
    password: SafePassword = attr(factory=SafePassword)
    income_history: IncomeHistory = attr(
        factory=lambda: resolve_class('backend.apps.entity.income.income_history',
                                  'IncomeHistory')())
    bill_history: BillHistory = attr(
        factory=lambda: resolve_class('backend.apps.entity.bill.bill_history',
                                  'BillHistory')())


    def save(self) -> 'User':
        saved_password: SafePassword = self.password.save()
        income_history: IncomeHistory = self.income_history.save()
        bill_history: BillHistory = self.bill_history.save()
        orm_model: UserOrmModel = self.get_orm_model()
        saved_user = UserOrmModel.objects.create(
            first_name=orm_model.first_name,
            last_name=orm_model.last_name,
            email=orm_model.email,
            username=orm_model.username,
            password=saved_password.get_orm_model(),
            income_history=income_history.get_orm_model(),
            bill_history=bill_history.get_orm_model()
        )
        return User.from_orm_model(saved_user)

    def update(self) -> None:
        try:
            db_model: UserOrmModel = UserOrmModel.objects.get(id=self.id)
            self.password.update()
            self.income_history.update()
            self.bill_history.update()
            orm_model: UserOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except UserOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        self.first_name = orm_model.first_name
        self.last_name = orm_model.last_name
        self.email = orm_model.email
        self.username = orm_model.username
        self.password = SafePassword.from_orm_model(orm_model.password)
        self.income_history = IncomeHistory.from_orm_model(orm_model.income_history)
        self.bill_history = BillHistory.from_orm_model(orm_model.bill_history)

    @staticmethod
    def set_orm_model(db_model, model_to_match) -> None:
        db_model.id = model_to_match.id
        db_model.first_name = model_to_match.first_name
        db_model.last_name = model_to_match.last_name
        db_model.username = model_to_match.username
        db_model.password = model_to_match.password
        db_model.income_history = model_to_match.income_history
        db_model.bill_history = model_to_match.bill_history

    def get_orm_model(self) -> UserOrmModel:
        return UserOrmModel(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            username=self.username,
            password=self.password.get_orm_model(),
            income_history=self.income_history.get_orm_model(),
            bill_history=self.bill_history.get_orm_model()
        )

    @staticmethod
    def from_orm_model(orm_model: UserOrmModel) -> 'User':
        user: User = User()
        user.set_from_orm_model(orm_model)
        return user