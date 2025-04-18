from backend.apps.entity.income.income_history import IncomeHistory


class IncomeHistoryRepository:
    def get_by_id(self, income_id: int) -> IncomeHistory:
        from backend.apps.entity.income.models import IncomeHistoryOrmModel
        orm_model: IncomeHistoryOrmModel = IncomeHistoryOrmModel.objects.get(id=income_id)
        return IncomeHistory.from_orm_model(orm_model)