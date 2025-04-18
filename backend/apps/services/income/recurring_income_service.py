from injector import inject

from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.repository.income.recurring_income_repository import \
    RecurringIncomeRepository


class RecurringIncomeService:
    @inject
    def __init__(self, recurring_income_repository: RecurringIncomeRepository):
        self.recurring_income_repository: RecurringIncomeRepository = recurring_income_repository

    def get_by_id(self, recurring_income_id: int) -> RecurringIncome:
        return self.recurring_income_repository.get_by_id(recurring_income_id)

    async def get_all_by_income_history(self, income_history) -> list[RecurringIncome]:
        return await self.recurring_income_repository.get_all_by_income_history(income_history)