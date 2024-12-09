from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.income_type import IncomeType
from backend.apps.entity.income.income_types import IncomeTypes
from backend.apps.entity.income.models import IncomeOrmModel
from backend.apps.entity.orm_compatible import OrmCompatible


@define
class Income(OrmCompatible['Income'], ABC, Identifiable):
    income: float = attr(default=0.0)
    income_type: IncomeType = attr(default=IncomeTypes.SALARY)

    def save(self) -> 'Income':
        saved_income_type = self.income_type.save()
        orm_model: IncomeOrmModel = self.get_orm_model()
        saved_income = IncomeOrmModel.objects.create(
            id=orm_model.id,
            income=orm_model.income,
            income_type=saved_income_type
        )
        return Income.from_orm_model(saved_income)

    def update(self):
        pass

    @staticmethod
    def from_orm_model(orm_model) -> 'Income':
        income = Income()
        income.income = orm_model.income
        income.income_type = IncomeType.from_orm_model(orm_model.income_type)
        return income

    def set_from_orm_model(self, orm_model) -> None:
        self.income = orm_model.income
        self.income_type = orm_model.income_type

    def get_orm_model(self) -> IncomeOrmModel:
        return IncomeOrmModel(
            income=self.income,
            income_type=self.income_type
        )
