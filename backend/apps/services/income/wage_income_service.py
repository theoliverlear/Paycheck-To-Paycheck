from injector import inject

from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.repository.income.wage_income_repository import \
    WageIncomeRepository


class WageIncomeService:
    @inject
    def __init__(self, wage_income_repository: WageIncomeRepository):
        self.wage_income_repository: WageIncomeRepository = wage_income_repository

    def get_by_id(self, wage_income_id: int):
        return self.wage_income_repository.get_by_id(wage_income_id)

    async def get_all_by_income_history(self, income_history: IncomeHistory) -> list[WageIncome]:
        return await self.wage_income_repository.get_all_by_income_history(income_history)