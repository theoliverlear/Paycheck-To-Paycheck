from typing import override

from attr import attr
from attrs import define
from channels.db import database_sync_to_async

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.bill.models import OneTimeBillOrmModel
from backend.apps.entity.bill.undated_bill import UndatedBill
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.due_date import DueDate
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class OneTimeBill(UndatedBill, OrmCompatible['OneTimeBill', OneTimeBillOrmModel]):
    due_date: DueDate = attr(factory=DueDate)
    bill_history: BillHistory = attr(default=None)

    @override
    async def save(self) -> 'OneTimeBill':
        if self.is_initialized():
            await self.update()
            return self
        else:
            saved_due_date: DueDate = await self.due_date.save()
            saved_bill_history: BillHistory = self.bill_history.save()
            orm_model: OneTimeBillOrmModel = self.get_orm_model()
            saved_bill: OneTimeBillOrmModel = await database_sync_to_async(OneTimeBillOrmModel.objects.create)(
                name=orm_model.name,
                amount=orm_model.amount,
                due_date=DueDate.get_orm_model(saved_due_date),
                bill_history= saved_bill_history.get_orm_model()
            )
            return OneTimeBill.from_orm_model(saved_bill)

    @override
    async def update(self) -> None:
        try:
            db_model: OneTimeBillOrmModel = await database_sync_to_async(OneTimeBillOrmModel.objects.get)(id=self.id)
            self.due_date.update()
            await self.bill_history.update()
            orm_model: OneTimeBillOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except OneTimeBillOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    @override
    def set_from_orm_model(self, orm_model: OneTimeBillOrmModel) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.amount = orm_model.amount
        self.due_date = DueDate.from_orm_model(orm_model.due_date)
        self.bill_history = BillHistory.from_orm_model(orm_model.bill_history)

    @override
    def get_orm_model(self) -> OneTimeBillOrmModel:
        return OneTimeBillOrmModel(
            id=self.id,
            name=self.name,
            amount=self.amount,
            due_date=self.due_date.get_orm_model(),
            bill_history=self.bill_history.get_orm_model()
        )

    @override
    @staticmethod
    def set_orm_model(db_model: OneTimeBillOrmModel,
                      model_to_match: OneTimeBillOrmModel) -> None:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.amount = model_to_match.amount
        db_model.due_date = model_to_match.due_date
        db_model.bill_history = model_to_match.bill_history

    @override
    @staticmethod
    def from_orm_model(orm_model: OneTimeBillOrmModel) -> 'OneTimeBill':
        bill = OneTimeBill()
        bill.set_from_orm_model(orm_model)
        return bill