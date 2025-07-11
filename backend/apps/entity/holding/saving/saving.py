from abc import ABC
from typing import override

from attr import attr
from attrs import define
from channels.db import database_sync_to_async

from backend.apps.entity.holding.holding import Holding
from backend.apps.entity.holding.saving.models import SavingOrmModel
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class Saving(Holding, OrmCompatible['Saving', SavingOrmModel]):
    @override
    async def save(self) -> 'Saving':
        if self.is_initialized():
            await self.update()
            return self
        else:
            saved_model: SavingOrmModel = await database_sync_to_async(SavingOrmModel.objects.create)(
                name=self.name,
                amount=self.amount
            )
            self.set_from_orm_model(saved_model)
            return Saving.from_orm_model(saved_model)

    @override
    async def update(self) -> None:
        try:
            db_model: SavingOrmModel = await database_sync_to_async(SavingOrmModel.objects.get)(id=self.id)
            orm_model: SavingOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            await database_sync_to_async(db_model.save)()
        except SavingOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    @override
    def set_from_orm_model(self, orm_model: SavingOrmModel) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.amount = orm_model.amount

    @override
    def get_orm_model(self) -> SavingOrmModel:
        return SavingOrmModel(
            id=self.id,
            name=self.name,
            amount=self.amount
        )

    @staticmethod
    @override
    def set_orm_model(db_model: SavingOrmModel,
                      model_to_match: SavingOrmModel) -> None:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.amount = model_to_match.amount

    @staticmethod
    @override
    def from_orm_model(orm_model: SavingOrmModel) -> 'Saving':
        saving: Saving = Saving()
        saving.set_from_orm_model(orm_model)
        return saving