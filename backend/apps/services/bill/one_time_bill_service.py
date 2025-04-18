from injector import inject

from backend.apps.entity.bill.one_time_bill import OneTimeBill
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