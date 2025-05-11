from channels.db import database_sync_to_async
from injector import inject

from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.user.user import User
from backend.apps.repository.income.one_time_income_repository import \
    OneTimeIncomeRepository


class OneTimeIncomeService:
    @inject
    def __init__(self, income_repository: OneTimeIncomeRepository):
        self.income_repository: OneTimeIncomeRepository = income_repository

    def get_by_id(self, income_id: int):
        return self.income_repository.get_by_id(income_id)

    async def get_all_by_income_history(self, income_history: IncomeHistory):
        return await self.income_repository.get_all_by_income_history(income_history)

    async def delete_from_user(self,
                               user: User,
                               income_id: int) -> None:
        user.user_income_history.one_time_incomes = [income for income in user.user_income_history.one_time_incomes if income.id != income_id]
        await user.user_income_history.save()
        await database_sync_to_async(self.income_repository.delete_by_id)(income_id)