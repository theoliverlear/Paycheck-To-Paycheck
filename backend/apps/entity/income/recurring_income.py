from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.income.income import Income
from backend.apps.entity.income.income_type import IncomeType
from backend.apps.entity.income.models import RecurringIncomeOrmModel
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class RecurringIncome(Income, OrmCompatible['RecurringIncome'], ABC):
    recurring_date: RecurringDate = attr(factory=RecurringDate)

    def save(self) -> 'RecurringIncome':
        saved_recurring_date: RecurringDate = self.recurring_date.save()
        income_type: IncomeType = self.income_type.save()
        orm_model: RecurringIncomeOrmModel = self.get_orm_model()
        saved_recurring_income: RecurringIncomeOrmModel = RecurringIncomeOrmModel.objects.create(
            income=orm_model.income,
            income_type=income_type.get_orm_model(),
            recurring_date=saved_recurring_date.get_orm_model()
        )
        return RecurringIncome.from_orm_model(saved_recurring_income)

    def update(self) -> None:
        try:
            db_model = RecurringIncomeOrmModel.objects.get(id=self.id)
            self.recurring_date.update()
            orm_model: RecurringIncomeOrmModel = self.get_orm_model()
            db_model: RecurringIncomeOrmModel = self.set_orm_model(db_model, orm_model)
            db_model.save()
        except RecurringIncomeOrmModel.DoesNotExist as exception:
            raise EntityNotFoundException(self)

    @staticmethod
    def set_orm_model(db_model, model_to_match) -> RecurringIncomeOrmModel:
        db_model.income = model_to_match.income
        db_model.income_type = model_to_match.income_type
        db_model.recurring_date = model_to_match.recurring_date
        return db_model

    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        self.income = orm_model.income
        self.income_type = IncomeType.from_orm_model(orm_model.income_type)
        self.recurring_date = RecurringDate.from_orm_model(orm_model.recurring_date)

    def get_orm_model(self) -> RecurringIncomeOrmModel:
        return RecurringIncomeOrmModel(
            id=self.id,
            income=self.income,
            income_type=self.income_type.get_orm_model(),
            recurring_date=self.recurring_date.get_orm_model()
        )

    @staticmethod
    def from_orm_model(orm_model: RecurringIncomeOrmModel) -> 'RecurringIncome':
        recurring_income: RecurringIncome = RecurringIncome()
        recurring_income.set_from_orm_model(orm_model)
        return recurring_income

