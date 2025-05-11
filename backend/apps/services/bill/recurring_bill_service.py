from channels.db import database_sync_to_async
from injector import inject

from backend.apps.entity.bill.recurring_bill import RecurringBill
from backend.apps.entity.user.user import User
from backend.apps.repository.bill.recurring_bill_repository import \
    RecurringBillRepository


class RecurringBillService:
    @inject
    def __init__(self,
                 recurring_bill_repository: RecurringBillRepository):
        self.recurring_bill_repository: RecurringBillRepository = recurring_bill_repository

    def get_by_id(self, recurring_bill_id: int) -> RecurringBill:
        return self.recurring_bill_repository.get_by_id(recurring_bill_id)

    async def get_all_by_bill_history(self, bill_history) -> list[RecurringBill]:
        return await self.recurring_bill_repository.get_all_by_bill_history(bill_history)

    async def delete_from_user(self,
                               user: User,
                               bill_id: int) -> None:
        user.user_bill_history.recurring_bills = []
        for bill in user.user_bill_history.recurring_bills:
            if bill.id != bill_id:
                user.user_bill_history.recurring_bills.append(bill)
        await user.user_bill_history.save()
        await database_sync_to_async(self.recurring_bill_repository.delete_by_id)(bill_id)