from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.date_interval import DateInterval
from backend.apps.entity.time.models import RecurringDateOrmModel


@define
class RecurringDate(OrmCompatible, ABC):
    day: int = attr(default=1)
    interval: DateInterval = attr(default=DateInterval.MONTHLY)

    def save(self):
        orm_model: RecurringDateOrmModel = self.get_orm_model()
        orm_model.save()

    def set_from_orm_model(self, orm_model):
        self.day = orm_model.day
        self.interval = DateInterval.from_interval(orm_model.interval)

    def get_orm_model(self):
        return RecurringDateOrmModel(
            day=self.day,
            interval=self.interval.value
        )