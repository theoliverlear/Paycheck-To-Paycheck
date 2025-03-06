from __future__ import annotations
from abc import ABC
from typing import override

from attr import attr
from attrs import define
from channels.db import database_sync_to_async

from backend.apps.entity.identifiable import Identifiable

from backend.apps.entity.bill.bill_history import BillHistory
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
    user_income_history: IncomeHistory = attr(default=None)
    user_bill_history: BillHistory = attr(default=None)

    def handle_uninstantiated_fields(self):
        if not self.user_income_history:
            self.user_income_history = IncomeHistory()
        if not self.user_bill_history:
            self.user_bill_history = BillHistory()
    @override
    async def save(self) -> 'User':
        if self.is_initialized():
            self.update()
            return self
        else:
            saved_password: SafePassword = await self.password.save()
            self.handle_uninstantiated_fields()
            user_income_history: IncomeHistory = await database_sync_to_async(self.user_income_history.save)()
            user_bill_history: BillHistory = await database_sync_to_async(self.user_bill_history.save)()
            orm_model: UserOrmModel = self.get_orm_model()
            saved_user = await database_sync_to_async(UserOrmModel.objects.create)(
                first_name=orm_model.first_name,
                last_name=orm_model.last_name,
                email=orm_model.email,
                username=orm_model.username,
                password=saved_password.get_orm_model(),
                income_history=user_income_history.get_orm_model(),
                bill_history=user_bill_history.get_orm_model()
            )
            self.set_from_orm_model(saved_user)
            return User.from_orm_model(saved_user)

    @override
    def update(self) -> None:
        try:
            db_model: UserOrmModel = UserOrmModel.objects.get(id=self.id)
            self.password.update()
            self.user_income_history.update()
            self.user_bill_history.update()
            orm_model: UserOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except UserOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    @override
    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        self.first_name = orm_model.first_name
        self.last_name = orm_model.last_name
        self.email = orm_model.email
        self.username = orm_model.username
        self.password = SafePassword.from_orm_model(orm_model.password)
        self.user_income_history = IncomeHistory.from_orm_model(orm_model.income_history)
        self.user_bill_history = BillHistory.from_orm_model(orm_model.bill_history)

    @override
    @staticmethod
    def set_orm_model(db_model, model_to_match) -> None:
        db_model.id = model_to_match.id
        db_model.first_name = model_to_match.first_name
        db_model.last_name = model_to_match.last_name
        db_model.email = model_to_match.email
        db_model.username = model_to_match.username
        db_model.password = model_to_match.password
        db_model.income_history = model_to_match.income_history
        db_model.bill_history = model_to_match.bill_history

    @override
    def get_orm_model(self) -> UserOrmModel:
        return UserOrmModel(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            username=self.username,
            password=self.password.get_orm_model(),
            income_history=self.user_income_history.get_orm_model(),
            bill_history=self.user_bill_history.get_orm_model()
        )

    @override
    @staticmethod
    def from_orm_model(orm_model: UserOrmModel) -> 'User':
        user: User = User()
        user.set_from_orm_model(orm_model)
        return user
