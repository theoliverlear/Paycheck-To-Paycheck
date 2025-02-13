from abc import ABC
from datetime import date, timedelta

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.time.models import RecurringDateOrmModel
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException
from backend.apps.models.date_utilities import get_tomorrow, get_next_week, \
    get_next_bi_week, get_next_month, get_next_year


@define
class RecurringDate(OrmCompatible['RecurringDate', RecurringDateOrmModel], ABC, Identifiable):
    day: date = attr(default=date.today())
    interval: YearInterval = attr(default=YearInterval.MONTHLY)

    def get_next_date(self) -> date:
        match self.interval:
            case YearInterval.DAILY:
                return get_tomorrow(self.day)
            case YearInterval.WEEKLY:
                return get_next_week(self.day)
            case YearInterval.BI_WEEKLY:
                return get_next_bi_week(self.day)
            case YearInterval.MONTHLY:
                return get_next_month(self.day)
            case YearInterval.YEARLY:
                return get_next_year(self.day)

    # ORM
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
        self.interval = YearInterval.from_interval(orm_model.interval)

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