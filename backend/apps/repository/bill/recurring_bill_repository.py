from channels.db import database_sync_to_async

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.bill.models import RecurringBillOrmModel, \
    BillHistoryOrmModel
from backend.apps.entity.bill.recurring_bill import RecurringBill


class RecurringBillRepository:
    def get_by_id(self, recurring_bill_id: int):
        # TODO: Probably needs to be async and then needs model instead of ORM
        #       model.
        return RecurringBillOrmModel.objects.filter(id=recurring_bill_id).first()

    def delete_by_id(self, recurring_bill_id: int) -> None:
        recurring_bill_orm_model: RecurringBillOrmModel = RecurringBillOrmModel.objects.filter(id=recurring_bill_id).first()
        if recurring_bill_orm_model:
            recurring_bill_orm_model.delete()

    async def get_all_by_bill_history(self, bill_history: BillHistory) -> list[RecurringBill]:
        bill_history_orm_model: BillHistoryOrmModel = bill_history.get_orm_model()
        orm_models: list[RecurringBillOrmModel] = await database_sync_to_async(lambda: list(RecurringBillOrmModel.objects.filter(
            bill_history=bill_history_orm_model
        )))()
        recurring_bills: list[RecurringBill] = []
        for orm_model in orm_models:
            recurring_bill: RecurringBill = await database_sync_to_async(RecurringBill.from_orm_model)(orm_model)
            recurring_bills.append(recurring_bill)
        return recurring_bills