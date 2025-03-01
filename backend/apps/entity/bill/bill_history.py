from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

from attr import attr
from attrs import define

from backend.apps.entity.bill.recurring_bill import RecurringBill
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException

if TYPE_CHECKING:
    from backend.apps.entity.bill.one_time_bill import OneTimeBill

from backend.apps.entity.bill.models import BillHistoryOrmModel
from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.orm_compatible import OrmCompatible

@define
class BillHistory(OrmCompatible['BillHistory', BillHistoryOrmModel], ABC, Identifiable):
    one_time_bills: list[OneTimeBill] = attr(default=[])
    recurring_bills: list[RecurringBill] = attr(default=[])

    def add_one_time_bill(self, bill: OneTimeBill) -> None:
        if bill not in self.one_time_bills:
            self.one_time_bills.append(bill)

    def add_recurring_bill(self, recurring_bill: RecurringBill) -> None:
        if recurring_bill not in self.recurring_bills:
            self.recurring_bills.append(recurring_bill)

    def save(self) -> 'BillHistory':
        if self.is_initialized():
            self.update()
            return self
        else:
            saved_bill_history = BillHistoryOrmModel.objects.create()
            self.set_from_orm_model(saved_bill_history)
            return BillHistory.from_orm_model(saved_bill_history)

    def update(self) -> None:
        try:
            db_model = BillHistoryOrmModel.objects.get(id=self.id)
            self.update_all_one_time_bills()
            self.update_all_recurring_bills()
            orm_model: BillHistoryOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except BillHistoryOrmModel.DoesNotExist as exception:
            raise EntityNotFoundException(self)

    def update_all_one_time_bills(self) -> None:
        for bill in self.one_time_bills:
            bill.update()

    def update_all_recurring_bills(self) -> None:
        for bill in self.recurring_bills:
            bill.update()

    def save_all_one_time_bills(self) -> list[OneTimeBill]:
        saved_bills = []
        for bill in self.one_time_bills:
            saved_bill: OneTimeBill = bill.save()
            saved_bills.append(saved_bill)
        self.one_time_bills = saved_bills
        return saved_bills

    def save_all_recurring_bills(self) -> list[RecurringBill]:
        saved_bills = []
        for bill in self.recurring_bills:
            saved_bill: RecurringBill = bill.save()
            saved_bills.append(saved_bill)
        self.recurring_bills = saved_bills
        return saved_bills

    def get_orm_model(self) -> BillHistoryOrmModel:
        one_time_bill_orm_models = [bill.get_orm_model() for bill in
                                    self.one_time_bills]
        recurring_bill_orm_models = [bill.get_orm_model() for
                                     bill in self.recurring_bills]
        return BillHistoryOrmModel(
            id=self.id
        )

    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        # self.set_one_time_bills_from_orm_model(orm_model)
        # self.set_recurring_bills_from_orm_model(orm_model)

    def set_recurring_bills_from_orm_model(self, orm_model):
        self.recurring_bills = []
        for bill in orm_model.recurring_bills:
            self.recurring_bills.append(
                RecurringBill.from_orm_model(bill))

    def set_one_time_bills_from_orm_model(self, orm_model):
        self.one_time_bills = []
        for bill in orm_model.one_time_bills:
            self.one_time_bills.append(OneTimeBill.from_orm_model(bill))

    @staticmethod
    def set_orm_model(db_model, model_to_match) -> None:
        db_model.id = model_to_match.id
        # db_model.one_time_bills = model_to_match.one_time_bills
        # db_model.recurring_bills = model_to_match.recurring_bills

    @staticmethod
    def from_orm_model(orm_model: BillHistoryOrmModel) -> 'BillHistory':
        bill_history = BillHistory()
        bill_history.set_from_orm_model(orm_model)
        return bill_history
