from injector import inject

from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.user.user import User
from backend.apps.repository.income.income_history_repository import \
    IncomeHistoryRepository
from backend.apps.services.income.one_time_income_service import \
    OneTimeIncomeService
from backend.apps.services.income.recurring_income_service import \
    RecurringIncomeService
from backend.apps.services.income.wage_income_service import WageIncomeService


class IncomeHistoryService:
    @inject
    def __init__(self, income_history_repository: IncomeHistoryRepository,
                 one_time_income_service: OneTimeIncomeService,
                 recurring_income_service: RecurringIncomeService,
                 wage_income_service: WageIncomeService):
        self.income_history_repository: IncomeHistoryRepository = income_history_repository
        self.one_time_income_service: OneTimeIncomeService = one_time_income_service
        self.recurring_income_service: RecurringIncomeService = recurring_income_service
        self.wage_income_service: WageIncomeService = wage_income_service

    def get_by_id(self, income_history_id: int):
        return self.income_history_repository.get_by_id(income_history_id)

    async def initialize_income_history(self, user: User) -> IncomeHistory:
        income_history: IncomeHistory = user.user_income_history
        user_one_time_incomes = await self.one_time_income_service.get_all_by_income_history(income_history)
        user_recurring_incomes = await self.recurring_income_service.get_all_by_income_history(income_history)
        user_wage_incomes = await self.wage_income_service.get_all_by_income_history(income_history)
        income_history.one_time_incomes = user_one_time_incomes
        income_history.recurring_incomes = user_recurring_incomes
        income_history.wage_incomes = user_wage_incomes
        return income_history