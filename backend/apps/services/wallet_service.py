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

    def save(self, wallet: Wallet):
        wallet.save()

    def update(self, wallet: Wallet):
        wallet.update()

    def save_or_update_wallet(self, wallet: Wallet):
        if wallet.is_initialized():
            self.update(wallet)
        else:
            self.save(wallet)
