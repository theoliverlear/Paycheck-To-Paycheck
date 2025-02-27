from __future__ import annotations

import logging
from abc import ABC
from typing import TYPE_CHECKING

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.models import IncomeHistoryOrmModel
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.orm_compatible import OrmCompatible

from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class IncomeHistory(OrmCompatible['IncomeHistory', IncomeHistoryOrmModel], ABC, Identifiable):
    one_time_incomes: list[OneTimeIncome] = attr(default=[])
    recurring_incomes: list[RecurringIncome] = attr(default=[])

    def add_one_time_income(self, income: OneTimeIncome) -> None:
        self.one_time_incomes.append(income)

    def add_recurring_income(self, recurring_income: RecurringIncome) -> None:
        self.recurring_incomes.append(recurring_income)

    def save(self) -> 'IncomeHistory':
        if self.is_initialized():
            self.update()
            return self
        else:
            saved_income_history = IncomeHistoryOrmModel.objects.create()
            self.set_from_orm_model(saved_income_history)
            self.save_all_one_time_incomes()
            self.save_all_recurring_incomes()
            return IncomeHistory.from_orm_model(saved_income_history)


    def update(self) -> None:
        try:
            db_model = IncomeHistoryOrmModel.objects.get(id=self.id)
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

    def get_orm_model(self) -> IncomeHistoryOrmModel:
        one_time_income_orm_models = [income.get_orm_model() for income in
                                      self.one_time_incomes]
        recurring_income_orm_models = [recurring_income.get_orm_model() for
                                       recurring_income in self.recurring_incomes]
        return IncomeHistoryOrmModel(
            id=self.id
        )

    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        # self.set_one_time_incomes_from_orm_model(orm_model)
        # self.set_recurring_incomes_from_orm_model(orm_model)

    def set_recurring_incomes_from_orm_model(self, orm_model):
        self.recurring_incomes = []
        for recurring_income in orm_model.recurring_incomes:
            self.recurring_incomes.append(
                RecurringIncome.from_orm_model(recurring_income))

    def set_one_time_incomes_from_orm_model(self, orm_model):
        self.one_time_incomes = []
        for income in orm_model.one_time_incomes:
            self.one_time_incomes.append(OneTimeIncome.from_orm_model(income))

    def save_all_one_time_incomes(self) -> list[OneTimeIncome]:
        saved_incomes = []
        for income in self.one_time_incomes:
            income.income_history = self
            saved_income: OneTimeIncome = income.save()
            saved_incomes.append(saved_income)
        self.one_time_incomes = saved_incomes
        return saved_incomes

    def save_all_recurring_incomes(self) -> list[RecurringIncome]:
        saved_recurring_incomes = []
        for recurring_income in self.recurring_incomes:
            recurring_income.income_history = self
            saved_recurring_income = recurring_income.save()
            saved_recurring_incomes.append(saved_recurring_income)
        self.recurring_incomes = saved_recurring_incomes
        return saved_recurring_incomes

    @staticmethod
    def set_orm_model(db_model: IncomeHistoryOrmModel, model_to_match: IncomeHistoryOrmModel) -> None:
        db_model.id = model_to_match.id

    @staticmethod
    def from_orm_model(orm_model: IncomeHistoryOrmModel) -> 'IncomeHistory':
        return IncomeHistory(id=orm_model.id)