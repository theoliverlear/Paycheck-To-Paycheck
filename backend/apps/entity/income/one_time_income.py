from __future__ import annotations
from abc import ABC
from datetime import date
from typing import TYPE_CHECKING, override

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
if TYPE_CHECKING:
    from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.models import OneTimeIncomeOrmModel
from backend.apps.entity.income.undated_income import UndatedIncome
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class OneTimeIncome(UndatedIncome, OrmCompatible['OneTimeIncome', OneTimeIncomeOrmModel], ABC, Identifiable):
    date_received: date = attr(default=date.today())
    income_history: IncomeHistory = attr(default=None)

    @override
    def save(self) -> 'OneTimeIncome':
        orm_model: OneTimeIncomeOrmModel = self.get_orm_model()
        saved_income = OneTimeIncomeOrmModel.objects.create(
            id=orm_model.id,
            name=orm_model.name,
            income_amount=orm_model.income_amount,
            date_received=orm_model.date_received,
            income_history=self.income_history.get_orm_model()
        )
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
        income.name = orm_model.name
        income.income_amount = orm_model.income_amount
        return income

    @override
    def set_from_orm_model(self, orm_model: OneTimeIncomeOrmModel) -> None:
        self.name = orm_model.name
        self.income_amount = orm_model.income_amount

    @override
    @staticmethod
    def set_orm_model(db_model: OneTimeIncomeOrmModel, model_to_match: OneTimeIncomeOrmModel) -> OneTimeIncomeOrmModel:
        db_model.name = model_to_match.name
        db_model.income_amount = model_to_match.income_amount
        return db_model

    @override
    def get_orm_model(self) -> OneTimeIncomeOrmModel:
        return OneTimeIncomeOrmModel(
            name=self.name,
            income_amount=self.income_amount,
            date_received=self.date_received,
            income_history=self.income_history.get_orm_model()
        )
