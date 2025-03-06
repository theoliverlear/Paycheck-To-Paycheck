from injector import inject

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.entity.user.user import User
from backend.apps.repository.user_repository import UserRepository


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def user_from_request(self, user_request: SignupRequest | LoginRequest) -> User:
        user: User = User(
            username=user_request.username,
            password=SafePassword(unhashed_password=user_request.password)
        )
        if isinstance(user_request, SignupRequest):
            user.email = user_request.email
        return user

    def get_by_username(self, username: str) -> User:
        return self.user_repository.get_by_username(username)