from channels.db import database_sync_to_async

from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.models import WageIncomeOrmModel, \
    IncomeHistoryOrmModel
from backend.apps.entity.income.wage_income import WageIncome


class WageIncomeRepository:
    def get_by_id(self, wage_income_id: int):
        return WageIncomeOrmModel.objects.filter(id=wage_income_id).first()

    async def get_all_by_income_history(self, income_history: IncomeHistory) -> list[WageIncome]:
        income_history_orm_model: IncomeHistoryOrmModel = income_history.get_orm_model()
        orm_models: list[WageIncomeOrmModel] = await database_sync_to_async(lambda: list(WageIncomeOrmModel.objects.filter(
            income_history=income_history_orm_model
        )))()
        wage_incomes: list[WageIncome] = []
        for orm_model in orm_models:
            wage_income: WageIncome = await database_sync_to_async(WageIncome.from_orm_model)(orm_model)
            wage_incomes.append(wage_income)
        return wage_incomes