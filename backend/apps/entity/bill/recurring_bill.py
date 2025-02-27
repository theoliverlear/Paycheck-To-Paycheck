from __future__ import annotations

from typing import TYPE_CHECKING

from attr import attr
from attrs import define

if TYPE_CHECKING:
    from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.bill.models import RecurringBillOrmModel, \
    BillHistoryOrmModel
from backend.apps.entity.bill.undated_bill import UndatedBill
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class RecurringBill(UndatedBill, OrmCompatible['RecurringBill', RecurringBillOrmModel]):
    recurring_date: RecurringDate = attr(factory=RecurringDate)
    bill_history: BillHistory = attr(default=None)

    def save(self) -> 'RecurringBill':
        if self.is_initialized():
            self.update()
            return self
        saved_recurring_date: RecurringDate = self.recurring_date.save()
        saved_bill_history: BillHistory = self.bill_history.save()
        saved_bill_history_orm: BillHistoryOrmModel = saved_bill_history.get_orm_model()
        orm_model: RecurringBillOrmModel = self.get_orm_model()
        saved_bill: RecurringBillOrmModel = RecurringBillOrmModel.objects.create(
            name=orm_model.name,
            amount=orm_model.amount,
            recurring_date=saved_recurring_date,
            bill_history=saved_bill_history_orm
        )
        return RecurringBill.from_orm_model(saved_bill)

    def update(self) -> None:
        try:
            db_model: RecurringBillOrmModel = RecurringBillOrmModel.objects.get(id=self.id)
            self.recurring_date.update()
            self.bill_history.update()
            orm_model: RecurringBillOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except RecurringBillOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    def set_from_orm_model(self, orm_model: RecurringBillOrmModel) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.amount = orm_model.amount
        self.recurring_date = RecurringDate.from_orm_model(orm_model.recurring_date)
        self.bill_history = BillHistory.from_orm_model(orm_model.bill_history)

    def get_orm_model(self) -> RecurringBillOrmModel:
        return RecurringBillOrmModel(
            id=self.id,
            name=self.name,
            amount=self.amount,
            recurring_date=self.recurring_date.get_orm_model(),
            bill_history=self.bill_history.get_orm_model()
        )

    @staticmethod
    def set_orm_model(db_model: RecurringBillOrmModel,
                      model_to_match: RecurringBillOrmModel) -> None:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.amount = model_to_match.amount
        db_model.recurring_date = model_to_match.recurring_date
        db_model.bill_history = model_to_match.bill_history

    @staticmethod
    def from_orm_model(orm_model: RecurringBillOrmModel) -> 'RecurringBill':
        bill = RecurringBill()
        bill.set_from_orm_model(orm_model)
        return bill