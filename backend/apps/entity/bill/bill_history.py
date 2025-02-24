from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

from attr import attr

from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.bill.recurring_bill import RecurringBill

if TYPE_CHECKING:
    from backend.apps.entity.user.user import User

from backend.apps.entity.bill.models import BillHistoryOrmModel
from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.orm_compatible import OrmCompatible


class BillHistory(OrmCompatible['BillHistory', BillHistoryOrmModel], ABC, Identifiable):
    user: 'User' = attr(factory=lambda: 'User()')
    one_time_bills: list[OneTimeBill] = attr(factory=list[OneTimeBill])
    recurring_bills: list[RecurringBill] = attr(factory=list[RecurringBill])

    def add_one_time_bill(self, bill: OneTimeBill) -> None:
        self.one_time_bills.append(bill)

    def add_recurring_bill(self, recurring_bill: RecurringBill) -> None:
        self.recurring_bills.append(recurring_bill)

    def save(self) -> 'BillHistory':
        saved_user: User = self.user.save()
        saved_one_time_bills: list[OneTimeBill] = self.save_all_one_time_bills()
        saved_recurring_bills: list[RecurringBill] = self.save_all_recurring_bills()
        orm_model: BillHistoryOrmModel = self.get_orm_model()
        saved_bill_history = BillHistoryOrmModel.objects.create(
            user=saved_user.get_orm_model(),
            one_time_bills=saved_one_time_bills,
            recurring_bills=saved_recurring_bills
        )
        return BillHistory.from_orm_model(saved_bill_history)

    def update(self) -> None:
        try:
            db_model = BillHistoryOrmModel.objects.get(id=self.id)
            self.user.update()
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
            saved_bills.append(bill.save())
        return saved_bills

    def save_all_recurring_bills(self) -> list[RecurringBill]:
        saved_bills = []
        for bill in self.recurring_bills:
            saved_bills.append(bill.save())
        return saved_bills

    def get_orm_model(self) -> BillHistoryOrmModel:
        one_time_bill_orm_models = [bill.get_orm_model() for bill in
                                    self.one_time_bills]
        recurring_bill_orm_models = [bill.get_orm_model() for
                                     bill in self.recurring_bills]
        return BillHistoryOrmModel(
            id=self.id,
            user=self.user.get_orm_model(),
            one_time_bills=one_time_bill_orm_models,
            recurring_bills=recurring_bill_orm_models
        )

    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        self.user = User.from_orm_model(orm_model.user)
        self.set_one_time_bills_from_orm_model(orm_model)
        self.set_recurring_bills_from_orm_model(orm_model)

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
        db_model.user = model_to_match.user
        db_model.one_time_bills = model_to_match.one_time_bills
        db_model.recurring_bills = model_to_match.recurring_bills

    @staticmethod
    def from_orm_model(orm_model: BillHistoryOrmModel) -> 'BillHistory':
        bill_history = BillHistory()
        bill_history.set_from_orm_model(orm_model)
        return bill_history
