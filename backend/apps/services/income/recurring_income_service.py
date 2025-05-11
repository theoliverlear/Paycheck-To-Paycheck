from channels.db import database_sync_to_async
from injector import inject

from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.user.user import User
from backend.apps.repository.income.recurring_income_repository import \
    RecurringIncomeRepository


class RecurringIncomeService:
    @inject
    def __init__(self,
                 recurring_income_repository: RecurringIncomeRepository):
        self.recurring_income_repository: RecurringIncomeRepository = recurring_income_repository

    def get_by_id(self, recurring_income_id: int) -> RecurringIncome:
        return self.recurring_income_repository.get_by_id(recurring_income_id)

    async def get_all_by_income_history(self, income_history) -> list[RecurringIncome]:
        return await self.recurring_income_repository.get_all_by_income_history(income_history)

    async def delete_from_user(self,
                               user: User,
                               recurring_income_id: int) -> None:
        user.user_income_history.recurring_incomes = []
        for recurring_income in user.user_income_history.recurring_incomes:
            if recurring_income.id != recurring_income_id:
                user.user_income_history.recurring_incomes.append(
                    recurring_income)
        await user.user_income_history.save()
        await database_sync_to_async(
            self.recurring_income_repository.delete_by_id)(recurring_income_id)