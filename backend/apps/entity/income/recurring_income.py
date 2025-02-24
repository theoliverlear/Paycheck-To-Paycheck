from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.income.models import RecurringIncomeOrmModel
from backend.apps.entity.income.undated_income import UndatedIncome
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class RecurringIncome(UndatedIncome, OrmCompatible['RecurringIncome', RecurringIncomeOrmModel], ABC):
    recurring_date: RecurringDate = attr(factory=RecurringDate)

    def save(self) -> 'RecurringIncome':
        saved_recurring_date: RecurringDate = self.recurring_date.save()
        orm_model: RecurringIncomeOrmModel = self.get_orm_model()
        saved_recurring_income: RecurringIncomeOrmModel = RecurringIncomeOrmModel.objects.create(
            name=orm_model.name,
            income_amount=orm_model.income_amount,
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
    def set_orm_model(db_model: RecurringIncomeOrmModel,
                      model_to_match: RecurringIncomeOrmModel) -> RecurringIncomeOrmModel:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.income_amount = model_to_match.income_amount
        db_model.recurring_date = model_to_match.recurring_date
        return db_model

    def set_from_orm_model(self, orm_model: RecurringIncomeOrmModel) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.income_amount = orm_model.income_amount
        self.recurring_date = RecurringDate.from_orm_model(orm_model.recurring_date)

    def get_orm_model(self) -> RecurringIncomeOrmModel:
        return RecurringIncomeOrmModel(
            id=self.id,
            name=self.name,
            income_amount=self.income_amount,
            recurring_date=self.recurring_date.get_orm_model()
        )

    @staticmethod
    def from_orm_model(orm_model: RecurringIncomeOrmModel) -> 'RecurringIncome':
        recurring_income: RecurringIncome = RecurringIncome()
        recurring_income.set_from_orm_model(orm_model)
        return recurring_income

