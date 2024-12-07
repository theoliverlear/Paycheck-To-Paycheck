from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.date_interval import DateInterval
from backend.apps.entity.time.models import RecurringDateOrmModel
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class RecurringDate(OrmCompatible, ABC, Identifiable):
    day: int = attr(default=1)
    interval: DateInterval = attr(default=DateInterval.MONTHLY)
    def save(self) -> 'RecurringDate':
        orm_model: RecurringDateOrmModel = self.get_orm_model()
        saved_recurring_date_orm: RecurringDateOrmModel = RecurringDateOrmModel.objects.create(
            day=self.day,
            interval=orm_model.interval
        )
        saved_recurring_date: RecurringDate = RecurringDate.from_orm_model(saved_recurring_date_orm)
        return saved_recurring_date

    def update(self) -> None:
        try:
            db_model: RecurringDateOrmModel = RecurringDateOrmModel.objects.get(id=self.id)
            orm_model: RecurringDateOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except RecurringDateOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    @staticmethod
    def set_orm_model(db_model, model_to_match) -> None:
        db_model.day = model_to_match.day
        db_model.interval = model_to_match.interval

    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        self.day = orm_model.day
        self.interval = DateInterval.from_interval(orm_model.interval)

    def get_orm_model(self) -> RecurringDateOrmModel:
        return RecurringDateOrmModel(
            id=self.id,
            day=self.day,
            interval=self.interval.value
        )
    @staticmethod
    def from_orm_model(orm_model: RecurringDateOrmModel) -> 'RecurringDate':
        recurring_date = RecurringDate()
        recurring_date.set_from_orm_model(orm_model)
        return recurring_date