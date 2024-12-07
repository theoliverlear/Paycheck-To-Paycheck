from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.models import IncomeTypeOrmModel
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.date_interval import DateInterval
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class IncomeType(Identifiable, OrmCompatible, ABC):
    name: str = attr(default="")
    interval: DateInterval = attr(default=DateInterval.MONTHLY)

    @staticmethod
    def set_orm_model(db_model, model_to_set) -> IncomeTypeOrmModel:
        db_model.id = model_to_set.id
        db_model.name = model_to_set.name
        db_model.interval = model_to_set.interval
        return db_model

    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.interval = DateInterval.from_interval(orm_model.interval)

    def update(self) -> None:
        try:
            db_model: IncomeTypeOrmModel = IncomeTypeOrmModel.objects.get(id=self.id)
            orm_model: IncomeTypeOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except Exception as exception:
            raise EntityNotFoundException(self)

    def save(self) -> 'IncomeType':
        orm_model: IncomeTypeOrmModel = self.get_orm_model()
        saved_income_type: IncomeTypeOrmModel = IncomeTypeOrmModel.objects.create(
            name=orm_model.name,
            interval=orm_model.interval
        )
        return IncomeType.from_orm_model(saved_income_type)

    def get_orm_model(self) -> IncomeTypeOrmModel:
        return IncomeTypeOrmModel(
            id=self.id,
            name=self.name,
            interval=self.interval.value
        )
    @staticmethod
    def from_orm_model(orm_model) -> 'IncomeType':
        income_type: IncomeType = IncomeType()
        income_type.set_from_orm_model(orm_model)
        return income_type