from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.bill.models import BillHistoryOrmModel


class BillHistoryRepository:
    def get_by_id(self, bill_history_id: int) -> BillHistory:
        return BillHistoryOrmModel.objects.filter(id=bill_history_id).first()