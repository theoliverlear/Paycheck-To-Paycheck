from channels.db import database_sync_to_async
from injector import inject

from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.user.user import User
from backend.apps.repository.bill.one_time_bill_repository import \
    OneTimeBillRepository


class OneTimeBillService:
    @inject
    def __init__(self,
                 one_time_bill_repository: OneTimeBillRepository):
        self.one_time_bill_repository: OneTimeBillRepository = one_time_bill_repository

    def get_by_id(self, one_time_bill_id: int) -> OneTimeBill:
        return self.one_time_bill_repository.get_by_id(one_time_bill_id)

    async def get_all_by_bill_history(self, bill_history) -> list[OneTimeBill]:
        return await self.one_time_bill_repository.get_all_by_bill_history(bill_history)

    async def delete_from_user(self,
                               user: User,
                               bill_id: int) -> None:
        user.user_bill_history.one_time_bills = [bill for bill in user.user_bill_history.one_time_bills if bill.id != bill_id]
        await user.user_bill_history.save()
        await database_sync_to_async(self.one_time_bill_repository.delete_by_id)(bill_id)