from __future__ import annotations

from abc import ABC
from typing import override

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.models import IncomeHistoryOrmModel
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.entity.orm_compatible import OrmCompatible

from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException

@define
class IncomeHistory(OrmCompatible['IncomeHistory', IncomeHistoryOrmModel], ABC, Identifiable):
    one_time_incomes: list[OneTimeIncome] = attr(default=[])
    recurring_incomes: list[RecurringIncome] = attr(default=[])
    wage_incomes: list[WageIncome] = attr(default=[])

    def add_one_time_income(self, income: OneTimeIncome) -> None:
        if income not in self.one_time_incomes:
            self.one_time_incomes.append(income)

    def add_recurring_income(self, recurring_income: RecurringIncome) -> None:
        if recurring_income not in self.recurring_incomes:
            self.recurring_incomes.append(recurring_income)

    def add_wage_income(self, wage_income: WageIncome) -> None:
        if wage_income not in self.wage_incomes:
            self.wage_incomes.append(wage_income)


    @override
    def save(self) -> 'IncomeHistory':
        if self.is_initialized():
            self.update()
            return self
        else:
            saved_income_history: IncomeHistoryOrmModel = IncomeHistoryOrmModel.objects.create()
            self.set_from_orm_model(saved_income_history)
            return IncomeHistory.from_orm_model(saved_income_history)

    def save_all(self) -> 'IncomeHistory':
        if self.is_initialized():
            self.update_all()
            return self
        else:
            saved_income_history = IncomeHistoryOrmModel.objects.create()
            self.set_from_orm_model(saved_income_history)
            self.save_all_one_time_incomes()
            self.save_all_recurring_incomes()
            return IncomeHistory.from_orm_model(saved_income_history)

    @override
    def update(self) -> None:
        try:
            db_model: IncomeHistoryOrmModel = IncomeHistoryOrmModel.objects.get(id=self.id)
            orm_model: IncomeHistoryOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except IncomeHistoryOrmModel.DoesNotExist as exception:
            raise EntityNotFoundException(self)

    def update_all(self) -> None:
        try:
            db_model: IncomeHistoryOrmModel = IncomeHistoryOrmModel.objects.get(id=self.id)
            self.update_all_one_time_incomes()
            self.update_all_recurring_incomes()
            orm_model: IncomeHistoryOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except IncomeHistoryOrmModel.DoesNotExist as exception:
            raise EntityNotFoundException(self)

    def update_all_one_time_incomes(self) -> None:
        for income in self.one_time_incomes:
            income.income_history = self
            income.update()

    def update_all_recurring_incomes(self) -> None:
        for recurring_income in self.recurring_incomes:
            recurring_income.income_history = self
            recurring_income.update()

    def update_all_wage_incomes(self) -> None:
        for wage_income in self.wage_incomes:
            wage_income.income_history = self
            wage_income.update()

    @override
    def get_orm_model(self) -> IncomeHistoryOrmModel:
        return IncomeHistoryOrmModel(
            id=self.id
        )

    @override
    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id

    def save_all_one_time_incomes(self) -> list[OneTimeIncome]:
        saved_incomes: list[OneTimeIncome] = []
        for income in self.one_time_incomes:
            income.income_history = self
            saved_income: OneTimeIncome = income.save()
            saved_incomes.append(saved_income)
        self.one_time_incomes = saved_incomes
        return saved_incomes

    def save_all_recurring_incomes(self) -> list[RecurringIncome]:
        saved_recurring_incomes: list[RecurringIncome] = []
        for recurring_income in self.recurring_incomes:
            recurring_income.income_history = self
            saved_recurring_income = recurring_income.save()
            saved_recurring_incomes.append(saved_recurring_income)
        self.recurring_incomes = saved_recurring_incomes
        return saved_recurring_incomes

    def save_all_wage_incomes(self) -> list[WageIncome]:
        saved_wage_incomes: list[WageIncome] = []
        for wage_income in self.wage_incomes:
            wage_income.income_history = self
            saved_wage_income = wage_income.save()
            saved_wage_incomes.append(saved_wage_income)
        self.wage_incomes = saved_wage_incomes
        return saved_wage_incomes


    @staticmethod
    @override
    def set_orm_model(db_model: IncomeHistoryOrmModel, model_to_match: IncomeHistoryOrmModel) -> None:
        db_model.id = model_to_match.id

    @staticmethod
    @override
    def from_orm_model(orm_model: IncomeHistoryOrmModel) -> 'IncomeHistory':
        return IncomeHistory(id=orm_model.id)