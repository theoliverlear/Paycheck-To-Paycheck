from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.income.income_type import IncomeType
from backend.apps.entity.income.income_types import IncomeTypes
from backend.apps.entity.income.models import IncomeOrmModel
from backend.apps.entity.orm_compatible import OrmCompatible


@define
class Income(OrmCompatible, ABC):
    income: float = attr(default=0.0)
    income_type: IncomeType = attr(default=IncomeTypes.SALARY)

    def save(self):
        orm_model: IncomeOrmModel = self.get_orm_model()
        orm_model.save()

    def set_from_orm_model(self, orm_model):
        self.income = orm_model.income
        self.income_type = orm_model.income_type

    def get_orm_model(self):
        return IncomeOrmModel(
            income=self.income,
            income_type=self.income_type
        )
