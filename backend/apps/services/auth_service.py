from injector import inject

from backend.apps.comm.request.user_request import UserRequest
from backend.apps.comm.response.auth_status import AuthStatus
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.entity.user.user import User
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.services.user_service import UserService


class AuthService:
    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def user_from_request(self, user_request: UserRequest):
        user: User = User(
            first_name=user_request.first_name,
            last_name=user_request.last_name,
            username=user_request.username,
            password=SafePassword(user_request.password)
        )
        return user

    def login(self, user_request: UserRequest) -> PayloadStatusResponse[AuthStatus]:
        user: User = self.user_from_request(user_request)
        user_from_db: User = self.user_service.get_by_username(user.username)
        password_matches: bool = user_from_db.password.compare_unencoded_password(user_request.password)
        if password_matches:
            return PayloadStatusResponse(
                payload=AuthStatus(is_authorized=True),
                status=200
            )
        else:
            return PayloadStatusResponse(
                payload=AuthStatus(is_authorized=False),
                status=401
            )
