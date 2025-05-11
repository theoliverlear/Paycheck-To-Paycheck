from datetime import date
from typing import override

from attr import attr
from attrs import define
from channels.db import database_sync_to_async

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.models import DueDateOrmModel
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class DueDate(Identifiable, OrmCompatible['DueDate', DueDateOrmModel]):
    due_date: date = attr(default=date.today())

    def is_due(self, date_to_check: date) -> bool:
        return self.due_date <= date_to_check

    def is_overdue(self, date_to_check: date) -> bool:
        return self.due_date < date_to_check

    def not_yet_due(self, date_to_check: date) -> bool:
        return self.due_date > date_to_check

    @override
    async def save(self) -> 'DueDate':
        orm_model: DueDateOrmModel = self.get_orm_model()
        saved_due_date = await database_sync_to_async(DueDateOrmModel.objects.create)(
            due_date=orm_model.due_date
        )
        return DueDate.from_orm_model(saved_due_date)

    @override
    async def update(self) -> None:
        try:
            db_model: DueDateOrmModel = await database_sync_to_async(DueDateOrmModel.objects.get)(id=self.id)
            orm_model: DueDateOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            await database_sync_to_async(db_model.save)()
        except DueDateOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    @override
    def set_from_orm_model(self, orm_model: DueDateOrmModel) -> None:
        self.id = orm_model.id
        self.due_date = orm_model.due_date

    @override
    @staticmethod
    def set_orm_model(db_model: DueDateOrmModel, model_to_match: DueDateOrmModel) -> None:
        db_model.id = model_to_match.id
        db_model.due_date = model_to_match.due_date

    @override
    def get_orm_model(self) -> DueDateOrmModel:
        return DueDateOrmModel(
            id=self.id,
            due_date=self.due_date
        )

    @override
    @staticmethod
    def from_orm_model(orm_model: DueDateOrmModel) -> 'DueDate':
        due_date = DueDate()
        due_date.set_from_orm_model(orm_model)
        return due_date