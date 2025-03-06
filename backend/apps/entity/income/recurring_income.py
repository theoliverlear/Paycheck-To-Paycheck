from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING, override

from attr import attr
from attrs import define
if TYPE_CHECKING:
    from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.models import RecurringIncomeOrmModel
from backend.apps.entity.income.undated_income import UndatedIncome
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class RecurringIncome(UndatedIncome, OrmCompatible['RecurringIncome', RecurringIncomeOrmModel], ABC):
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
    def income_amount(self):
        self.calculate_yearly_income()
        return self._income_amount

    @income_amount.setter
    def income_amount(self, income_amount):
        self._income_amount = income_amount
        self.calculate_yearly_income()

    def __attrs_post_init__(self):
        self.calculate_yearly_income()

    def calculate_yearly_income(self):
        self.yearly_income = self._income_amount * self._recurring_date.interval.value

    @override
    def save(self) -> 'RecurringIncome':
        if self.is_initialized():
            self.update()
            return self
        else:
            saved_recurring_date: RecurringDate = self._recurring_date.save()
            saved_income_history: IncomeHistory = self.income_history.save()
            orm_model: RecurringIncomeOrmModel = self.get_orm_model()
            saved_recurring_income: RecurringIncomeOrmModel = RecurringIncomeOrmModel.objects.create(
                name=orm_model.name,
                income_amount=orm_model.income_amount,
                recurring_date=saved_recurring_date.get_orm_model(),
                income_history=saved_income_history.get_orm_model()
            )
            return RecurringIncome.from_orm_model(saved_recurring_income)

    @override
    def update(self) -> None:
        try:
            db_model = RecurringIncomeOrmModel.objects.get(id=self.id)
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
        db_model.income_amount = model_to_match.income_amount
        db_model.recurring_date = model_to_match.recurring_date
        db_model.income_history = model_to_match.income_history
        return db_model

    @override
    def set_from_orm_model(self, orm_model: RecurringIncomeOrmModel) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.income_amount = orm_model.income_amount
        self.recurring_date = RecurringDate.from_orm_model(orm_model.recurring_date)
        self.income_history = orm_model.income_history.get_orm_model()

    @override
    def get_orm_model(self) -> RecurringIncomeOrmModel:
        return RecurringIncomeOrmModel(
            id=self.id,
            name=self.name,
            income_amount=self.income_amount,
            recurring_date=self.recurring_date.get_orm_model(),
            income_history=self.income_history.get_orm_model()
        )

    @override
    @staticmethod
    def from_orm_model(orm_model: RecurringIncomeOrmModel) -> 'RecurringIncome':
        recurring_income: RecurringIncome = RecurringIncome()
        recurring_income.set_from_orm_model(orm_model)
        return recurring_income

