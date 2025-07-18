from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING, override

from attr import attr
from attrs import define
from channels.db import database_sync_to_async

if TYPE_CHECKING:
    from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.models import RecurringIncomeOrmModel
from backend.apps.entity.income.undated_income import UndatedIncome
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class RecurringIncome(UndatedIncome, OrmCompatible['RecurringIncome', RecurringIncomeOrmModel]):
    _recurring_date: RecurringDate = attr(factory=RecurringDate)
    yearly_income: float = attr(default=0.0)
    income_history: IncomeHistory = attr(default=None)

    @property
    def recurring_date(self):
        self.calculate_yearly_income()
        return self._recurring_date

    @recurring_date.setter
    def recurring_date(self, recurring_date):
        self._recurring_date = recurring_date
        self.calculate_yearly_income()

    @property
    def amount(self):
        self.calculate_yearly_income()
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount
        self.calculate_yearly_income()

    def __attrs_post_init__(self):
        self.calculate_yearly_income()

    def calculate_yearly_income(self):
        self.yearly_income = self._amount * self._recurring_date.interval.value

    @override
    async def save(self) -> 'RecurringIncome':
        if self.is_initialized():
            self.update()
            return self
        else:
            saved_recurring_date: RecurringDate = await self._recurring_date.save()
            saved_income_history: IncomeHistory = await self.income_history.save()
            orm_model: RecurringIncomeOrmModel = self.get_orm_model()
            saved_recurring_income: RecurringIncomeOrmModel = await database_sync_to_async(RecurringIncomeOrmModel.objects.create)(
                name=orm_model.name,
                amount=orm_model.amount,
                recurring_date=saved_recurring_date.get_orm_model(),
                income_history=saved_income_history.get_orm_model()
            )
            self.set_from_orm_model(saved_recurring_income)
            return RecurringIncome.from_orm_model(saved_recurring_income)

    @override
    async def update(self) -> None:
        try:
            db_model = await database_sync_to_async(RecurringIncomeOrmModel.objects.get)(id=self.id)
            self._recurring_date.update()
            orm_model: RecurringIncomeOrmModel = self.get_orm_model()
            current_model: RecurringIncomeOrmModel = RecurringIncome.set_orm_model(db_model, orm_model)
            current_model.save()
        except RecurringIncomeOrmModel.DoesNotExist as exception:
            raise EntityNotFoundException(self)

    @override
    @staticmethod
    def set_orm_model(db_model: RecurringIncomeOrmModel,
                      model_to_match: RecurringIncomeOrmModel) -> RecurringIncomeOrmModel:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.amount = model_to_match.amount
        db_model.recurring_date = model_to_match.recurring_date
        db_model.income_history = model_to_match.income_history
        return db_model

    @override
    def set_from_orm_model(self, orm_model: RecurringIncomeOrmModel) -> None:
        from backend.apps.entity.income.income_history import IncomeHistory
        self.id = orm_model.id
        self.name = orm_model.name
        self.amount = orm_model.amount
        self.recurring_date = RecurringDate.from_orm_model(orm_model.recurring_date)
        self.income_history = IncomeHistory.from_orm_model(orm_model.income_history)

    @override
    def get_orm_model(self) -> RecurringIncomeOrmModel:
        return RecurringIncomeOrmModel(
            id=self.id,
            name=self.name,
            amount=self.amount,
            recurring_date=self.recurring_date.get_orm_model(),
            income_history=self.income_history.get_orm_model()
        )

    @override
    @staticmethod
    def from_orm_model(orm_model: RecurringIncomeOrmModel) -> 'RecurringIncome':
        recurring_income: RecurringIncome = RecurringIncome()
        recurring_income.set_from_orm_model(orm_model)
        return recurring_income

