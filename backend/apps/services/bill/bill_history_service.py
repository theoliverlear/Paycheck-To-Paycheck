from injector import inject

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.user.user import User
from backend.apps.repository.bill.bill_history_repository import \
    BillHistoryRepository
from backend.apps.services.bill.one_time_bill_service import \
    OneTimeBillService
from backend.apps.services.bill.recurring_bill_service import \
    RecurringBillService


class BillHistoryService:
    @inject
    def __init__(self,
                 bill_history_repository: BillHistoryRepository,
                 one_time_bill_service: OneTimeBillService,
                 recurring_bill_service: RecurringBillService):
        self.bill_history_repository: BillHistoryRepository = bill_history_repository
        self.one_time_bill_service: OneTimeBillService = one_time_bill_service
        self.recurring_bill_service: RecurringBillService = recurring_bill_service

    def get_by_id(self, bill_history_id: int) -> BillHistory:
        return self.bill_history_repository.get_by_id(bill_history_id)

    async def initialize_bill_history(self, user: User) -> BillHistory:
        bill_history: BillHistory = user.user_bill_history
        one_time_bills =  await self.one_time_bill_service.get_all_by_bill_history(bill_history)
        recurring_bills = await self.recurring_bill_service.get_all_by_bill_history(bill_history)
        bill_history.one_time_bills = one_time_bills
        bill_history.recurring_bills = recurring_bills
        return bill_history

