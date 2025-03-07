from abc import ABC
from typing import override

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.models import IncomeTypeOrmModel
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class IncomeType(Identifiable, OrmCompatible['IncomeType', IncomeTypeOrmModel], ABC):
    interval: YearInterval = attr(default=YearInterval.MONTHLY)

    @override
    @staticmethod
    def set_orm_model(db_model, model_to_match) -> IncomeTypeOrmModel:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.interval = model_to_match.interval
        return db_model

    @override
    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.interval = YearInterval.from_interval(orm_model.interval)

    @override
    def update(self) -> None:
        try:
            db_model: IncomeTypeOrmModel = IncomeTypeOrmModel.objects.get(id=self.id)
            orm_model: IncomeTypeOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except Exception as exception:
            raise EntityNotFoundException(self)

    @override
    def save(self) -> 'IncomeType':
        orm_model: IncomeTypeOrmModel = self.get_orm_model()
        saved_income_type: IncomeTypeOrmModel = IncomeTypeOrmModel.objects.create(
            name=orm_model.name,
            interval=orm_model.interval
        )
        return IncomeType.from_orm_model(saved_income_type)

    @override
    def get_orm_model(self) -> IncomeTypeOrmModel:
        return IncomeTypeOrmModel(
            id=self.id,
            name=self.name,
            interval=self.interval.value
        )

    @override
    @staticmethod
    def from_orm_model(orm_model) -> 'IncomeType':
        income_type: IncomeType = IncomeType()
        income_type.set_from_orm_model(orm_model)
        return income_type