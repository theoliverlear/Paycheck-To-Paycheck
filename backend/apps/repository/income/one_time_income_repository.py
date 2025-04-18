from typing import Optional

from channels.db import database_sync_to_async

from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.models import OneTimeIncomeOrmModel, \
    IncomeHistoryOrmModel
from backend.apps.entity.income.one_time_income import OneTimeIncome


class OneTimeIncomeRepository:
    def get_by_id(self, income_id: int) -> Optional[OneTimeIncome]:
        orm_model: OneTimeIncomeOrmModel = OneTimeIncomeOrmModel.objects.filter(id=income_id).first()
        return OneTimeIncome.from_orm_model(orm_model)

    async def get_all_by_income_history(self, income_history: IncomeHistory) -> list[OneTimeIncome]:
        income_history_orm_model: IncomeHistoryOrmModel = income_history.get_orm_model()
        orm_models: list[OneTimeIncomeOrmModel] = await database_sync_to_async(lambda: list(OneTimeIncomeOrmModel.objects.filter(
            income_history=income_history_orm_model
        )))()
        one_time_incomes: list[OneTimeIncome] = []
        for orm_model in orm_models:
            one_time_income: OneTimeIncome = await database_sync_to_async(OneTimeIncome.from_orm_model)(orm_model)
            one_time_incomes.append(one_time_income)
        return one_time_incomes
