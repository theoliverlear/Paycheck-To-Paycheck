from channels.db import database_sync_to_async

from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.models import IncomeHistoryOrmModel, \
    RecurringIncomeOrmModel
from backend.apps.entity.income.recurring_income import RecurringIncome


class RecurringIncomeRepository:
    def get_by_id(self, income_id: int):
        from backend.apps.entity.income.models import RecurringIncomeOrmModel
        orm_model: RecurringIncomeOrmModel = RecurringIncomeOrmModel.objects.get(id=income_id)
        return orm_model
    
    async def get_all_by_income_history(self, income_history: IncomeHistory) -> list[RecurringIncome]:
        income_history_orm_model: IncomeHistoryOrmModel = income_history.get_orm_model()
        orm_models: list[RecurringIncomeOrmModel] = await database_sync_to_async(lambda: list(RecurringIncomeOrmModel.objects.filter(
            income_history=income_history_orm_model
        )))()
        recurring_incomes: list[RecurringIncome] = []
        for orm_model in orm_models:
            recurring_income: RecurringIncome = await database_sync_to_async(RecurringIncome.from_orm_model)(orm_model)
            recurring_incomes.append(recurring_income)
        return recurring_incomes