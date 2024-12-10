from injector import inject
from rest_framework import status

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.entity.user.user import User
from backend.apps.models.http.auth_response import AuthResponse
from backend.apps.models.http.auth_status import AuthStatus
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.services.paycheck_to_paycheck_service import \
    PaycheckToPaycheckService
from backend.apps.services.user_service import UserService




class AuthService:
    @inject
    def __init__(self,
                 user_service: UserService,
                 paycheck_to_paycheck_service: PaycheckToPaycheckService):
        self.user_service = user_service
        self.paycheck_to_paycheck_service = paycheck_to_paycheck_service



    def signup(self, user_request: SignupRequest, http_request) -> PayloadStatusResponse[AuthStatusResponse]:
        user_in_session: bool = self.paycheck_to_paycheck_service.user_in_session(http_request)
        if user_in_session:
            return AuthResponse.IN_SESSION_CONFLICT.value
        user: User = self.user_service.user_from_request(user_request)
        user_from_db: User = self.user_service.get_by_username(user.username)
        if user_from_db:
            return AuthResponse.CONFLICT.value
        else:
            user: User = user.save()
            self.paycheck_to_paycheck_service.save_user_to_session(user, http_request)
            return AuthResponse.AUTHORIZED.value


    def login(self, user_request: LoginRequest, http_request) -> PayloadStatusResponse[AuthStatusResponse]:
        user_in_session: bool = self.paycheck_to_paycheck_service.user_in_session(http_request)
        if user_in_session:
            return AuthResponse.IN_SESSION_CONFLICT.value
        user: User = self.user_service.user_from_request(user_request)
        user_from_db: User = self.user_service.get_by_username(user.username)
        password_matches: bool = user_from_db.password.compare_unencoded_password(user_request.password)
        if password_matches:
            self.paycheck_to_paycheck_service.save_user_to_session(user, http_request)
            return AuthResponse.AUTHORIZED.value
        else:
            return AuthResponse.UNAUTHORIZED.value

    def logout(self, http_request) -> PayloadStatusResponse[AuthStatusResponse]:
        user_in_session: bool = self.paycheck_to_paycheck_service.user_in_session(http_request)
        if not user_in_session:
            return PayloadStatusResponse[AuthStatusResponse](
                payload=AuthStatusResponse(auth_status=AuthStatus.UNAUTHORIZED),
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        else:
            self.paycheck_to_paycheck_service.remove_user_from_session(http_request)
            return PayloadStatusResponse[AuthStatusResponse](
                payload=AuthStatusResponse(auth_status=AuthStatus.UNAUTHORIZED),
                status_code=status.HTTP_200_OK
            )
