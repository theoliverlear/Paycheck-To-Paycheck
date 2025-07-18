from __future__ import annotations
from abc import ABC
from datetime import date
from typing import TYPE_CHECKING, override

from attr import attr
from attrs import define
from channels.db import database_sync_to_async

from backend.apps.entity.identifiable import Identifiable
if TYPE_CHECKING:
    from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.models import OneTimeIncomeOrmModel
from backend.apps.entity.income.undated_income import UndatedIncome
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class OneTimeIncome(UndatedIncome, OrmCompatible['OneTimeIncome', OneTimeIncomeOrmModel], Identifiable):
    date_received: date = attr(default=date.today())
    income_history: IncomeHistory = attr(default=None)

    @override
    async def save(self) -> 'OneTimeIncome':
        income_history: IncomeHistory = await self.income_history.save()
        orm_model: OneTimeIncomeOrmModel = self.get_orm_model()
        saved_income = await database_sync_to_async(OneTimeIncomeOrmModel.objects.create)(
            id=orm_model.id,
            name=orm_model.name,
            amount=orm_model.amount,
            date_received=orm_model.date_received,
            income_history=income_history.get_orm_model()
        )
        self.set_from_orm_model(saved_income)
        return OneTimeIncome.from_orm_model(saved_income)

    @override
    def update(self):
        try:
            db_model = OneTimeIncomeOrmModel.objects.get(id=self.id)
            orm_model: OneTimeIncomeOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except OneTimeIncomeOrmModel.DoesNotExist as exception:
            raise EntityNotFoundException(self)

    @override
    @staticmethod
    def from_orm_model(orm_model: OneTimeIncomeOrmModel) -> 'OneTimeIncome':
        income = OneTimeIncome()
        income.id = orm_model.id
        income.name = orm_model.name
        income.amount = orm_model.amount
        return income

    @override
    def set_from_orm_model(self, orm_model: OneTimeIncomeOrmModel) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.amount = orm_model.amount

    @override
    @staticmethod
    def set_orm_model(db_model: OneTimeIncomeOrmModel, model_to_match: OneTimeIncomeOrmModel) -> OneTimeIncomeOrmModel:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.amount = model_to_match.amount
        return db_model

    @override
    def get_orm_model(self) -> OneTimeIncomeOrmModel:
        return OneTimeIncomeOrmModel(
            id=self.id,
            name=self.name,
            amount=self.amount,
            date_received=self.date_received,
            income_history=self.income_history.get_orm_model()
        )
