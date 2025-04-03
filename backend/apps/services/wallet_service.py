from injector import inject

from backend.apps.entity.user.user import User
from backend.apps.entity.wallet.wallet import Wallet
from backend.apps.repository.wallet_repository import WalletRepository


class WalletService:
    @inject
    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository: WalletRepository = wallet_repository

    def get_by_user(self, user: User) -> Wallet:
        return self.wallet_repository.get_by_user_id(user.id)