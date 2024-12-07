from injector import inject

from backend.apps.repository.user_repository import UserRepository


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
