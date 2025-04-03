from abc import ABC

from backend.apps.entity.user.models import UserOrmModel
from backend.apps.entity.wallet.models import WalletOrmModel
from backend.apps.entity.wallet.wallet import Wallet
from backend.apps.repository.database_accessible import DatabaseAccessible


class WalletRepository(DatabaseAccessible[Wallet], ABC):

    def get_by_user_id(self, user_id: int) -> Wallet:
        user_orm_model: UserOrmModel = UserOrmModel.objects.get(id=user_id)
        return Wallet.from_orm_model(user_orm_model.wallet)