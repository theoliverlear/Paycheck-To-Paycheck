from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.income.income import Income
from backend.apps.entity.income.models import RecurringIncomeOrmModel
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.recurring_date import RecurringDate

@define
class RecurringIncome(Income, OrmCompatible, ABC):
    recurring_date: RecurringDate = attr(factory=RecurringDate)

    def save(self):
        orm_model: RecurringIncomeOrmModel = self.get_orm_model()
        orm_model.save()

    def set_from_orm_model(self, orm_model):
        self.income = orm_model.income
        self.income_type = orm_model.income_type
        self.recurring_date = orm_model.recurring_date

    def get_orm_model(self):
        return RecurringIncomeOrmModel(
            income=self.income,
            income_type=self.income_type,
            recurring_date=self.recurring_date.get_orm_model()
        )

