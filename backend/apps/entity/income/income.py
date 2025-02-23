from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.models import IncomeOrmModel
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class Income(OrmCompatible['Income', IncomeOrmModel], ABC, Identifiable):
    name: str = attr(default="")
    income_amount: float = attr(default=0.0)

    def save(self) -> 'Income':
        orm_model: IncomeOrmModel = self.get_orm_model()
        saved_income = IncomeOrmModel.objects.create(
            id=orm_model.id,
            name=orm_model.name,
            income_amount=orm_model.income_amount,
        )
        return Income.from_orm_model(saved_income)

    def update(self):
        try:
            db_model = IncomeOrmModel.objects.get(id=self.id)
            orm_model: IncomeOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except IncomeOrmModel.DoesNotExist as exception:
            raise EntityNotFoundException(self)

    @staticmethod
    def from_orm_model(orm_model: IncomeOrmModel) -> 'Income':
        income = Income()
        income.name = orm_model.name
        income.income_amount = orm_model.income_amount
        return income

    def set_from_orm_model(self, orm_model: IncomeOrmModel) -> None:
        self.name = orm_model.name
        self.income_amount = orm_model.income_amount

    @staticmethod
    def set_orm_model(db_model: IncomeOrmModel, model_to_match: IncomeOrmModel) -> IncomeOrmModel:
        db_model.name = model_to_match.name
        db_model.income_amount = model_to_match.income_amount
        return db_model

    def get_orm_model(self) -> IncomeOrmModel:
        return IncomeOrmModel(
            name=self.name,
            income_amount=self.income_amount,
        )
