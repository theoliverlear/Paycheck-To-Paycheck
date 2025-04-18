from channels.db import database_sync_to_async

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.bill.models import OneTimeBillOrmModel, \
    BillHistoryOrmModel
from backend.apps.entity.bill.one_time_bill import OneTimeBill


class OneTimeBillRepository:
    def get_by_id(self, one_time_bill_id: int) -> OneTimeBill:
        return OneTimeBillOrmModel.objects.filter(id=one_time_bill_id).first()

    async def get_all_by_bill_history(self, bill_history: BillHistory) -> list[OneTimeBill]:
        bill_history_orm_model: BillHistoryOrmModel = bill_history.get_orm_model()
        orm_models: list[OneTimeBillOrmModel] = await database_sync_to_async(lambda: list(OneTimeBillOrmModel.objects.filter(
            bill_history=bill_history_orm_model
        )))()
        one_time_bills: list[OneTimeBill] = []
        for orm_model in orm_models:
            one_time_bill: OneTimeBill = await database_sync_to_async(OneTimeBill.from_orm_model)(orm_model)
            one_time_bills.append(one_time_bill)
        return one_time_bills