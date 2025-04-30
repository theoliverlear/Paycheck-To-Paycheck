# auth_service.py
from asgiref.sync import sync_to_async
from injector import inject
from rest_framework.response import Response

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.comm.response.operation_success_response import \
    OperationSuccessResponse
from backend.apps.entity.user.user import User
from backend.apps.models.http.auth_response import AuthResponse
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.operation_sucess_status import \
    OperationSuccessStatus
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.services.session.session_service import SessionService
from backend.apps.services.user_service import UserService
from backend.apps.services.session.websocket_session_service import \
    WebSocketSessionService


class AuthService:
    @inject
    def __init__(self,
                 user_service: UserService,
                 session_service: SessionService,
                 websocket_session_service: WebSocketSessionService):
        self.user_service: UserService = user_service
        self.session_service: SessionService = session_service
        self.websocket_session_service: WebSocketSessionService = websocket_session_service


    async def user_in_session(self,
                        communication_type = CommunicationType.HTTP,
                        http_request = None,
                        session_scope: dict = None):
        if communication_type == CommunicationType.HTTP:
            user_in_session: bool = self.session_service.user_in_session(http_request)
        else:
            user_in_session: bool= await self.websocket_session_service.user_in_session(session_scope)
        if user_in_session:
            return AuthResponse.AUTHORIZED.value
        else:
            return AuthResponse.UNAUTHORIZED.value

    async def is_logged_in(self,
                     communication_type: CommunicationType = CommunicationType.HTTP,
                     http_request = None,
                     session_scope: dict = None):
        if communication_type == CommunicationType.HTTP:
            return await self.user_in_session(communication_type, http_request=http_request)
        else:
            return await self.user_in_session(communication_type, session_scope=session_scope)

    async def signup(self,
                     signup_request: SignupRequest,
                     http_request = None,
                     session_scope: dict = None) -> PayloadStatusResponse[AuthStatusResponse]:
        if http_request is not None:
            return await self.http_signup(signup_request, http_request)
        else:
            return await self.websocket_signup(signup_request, session_scope)

    # TODO: Similar logic in HTTP and WebSocket can be combined
    async def http_signup(self,
                          signup_request: SignupRequest,
                          http_request) -> PayloadStatusResponse[AuthStatusResponse]:
        user_in_session: bool = self.session_service.user_in_session(http_request)
        if user_in_session:
            return AuthResponse.IN_SESSION_CONFLICT.value
        user: User = self.user_service.user_from_request(signup_request)
        user_from_db: User = await self.user_service.get_by_username(user.username)
        if user_from_db:
            return AuthResponse.CONFLICT.value
        else:
            user: User = await user.save()
            self.session_service.save_user_to_session(user, http_request)
            return AuthResponse.AUTHORIZED.value

    async def websocket_signup(self,
                               signup_request: SignupRequest,
                               session_scope: dict):
        user_in_session: bool = await self.websocket_session_service.user_in_session(session_scope)
        if user_in_session:
            return AuthResponse.IN_SESSION_CONFLICT.value
        user: User = self.user_service.user_from_request(signup_request)
        user_from_db: User = await self.user_service.get_by_username(user.username)
        if user_from_db:
            return AuthResponse.CONFLICT.value
        else:
            user: User = await user.save()
            await self.websocket_session_service.save_user_to_session(session_scope, user)
            return AuthResponse.AUTHORIZED.value


    async def login(self,
                    login_request: LoginRequest,
                    http_request = None,
                    session_scope: dict = None) -> PayloadStatusResponse[AuthStatusResponse]:
        if http_request:
            return await self.http_login(login_request, http_request)
        else:
            return await self.websocket_login(login_request, session_scope)

    async def http_login(self,
                         login_request: LoginRequest,
                         http_request) -> PayloadStatusResponse[AuthStatusResponse]:
        user_in_session: bool = self.session_service.user_in_session(
            http_request)
        if user_in_session:
            session_user: User = await self.session_service.get_user_from_session(http_request)
            if session_user.username == login_request.username:
                self.session_service.remove_user_from_session(http_request)
                return await self.http_login(login_request, http_request)
            return AuthResponse.IN_SESSION_CONFLICT.value
        user: User = self.user_service.user_from_request(login_request)
        db_user: User = await self.user_service.get_by_username(user.username)
        if db_user is None:
            return AuthResponse.UNAUTHORIZED.value

        password_matches: bool = db_user.password.compare_unencoded_password(login_request.password)

        if password_matches:
            await sync_to_async(self.session_service.save_user_to_session)(db_user, http_request)
            return AuthResponse.AUTHORIZED.value
        else:
            return AuthResponse.UNAUTHORIZED.value

    async def websocket_login(self,
                              login_request: LoginRequest,
                              session_scope: dict) -> PayloadStatusResponse[AuthStatusResponse]:
        user_in_session: bool = await self.websocket_session_service.user_in_session(session_scope)
        if user_in_session:
            return AuthResponse.IN_SESSION_CONFLICT.value
        user: User = self.user_service.user_from_request(login_request)
        # db_user: User = self.user_service.get_by_username(user.username)
        db_user = await self.user_service.get_by_username(user.username)
        if db_user:
            password_matches: bool = db_user.password.compare_unencoded_password(login_request.password)
            if password_matches:
                await self.websocket_session_service.save_user_to_session(session_scope, db_user)
                return AuthResponse.AUTHORIZED.value
            else:
                return AuthResponse.UNAUTHORIZED.value
        else:
            return AuthResponse.UNAUTHORIZED.value

    async def logout(self,
               communication_type: CommunicationType = CommunicationType.HTTP,
               http_request = None,
               session_scope: dict = None) -> PayloadStatusResponse[OperationSuccessResponse]:
        if communication_type == CommunicationType.HTTP:
            return await self.http_logout(http_request)
        else:
            return await self.websocket_logout(session_scope)


    async def http_logout(self, http_request) -> PayloadStatusResponse[OperationSuccessResponse]:
        if self.session_service.user_in_session(http_request):
            await sync_to_async(self.session_service.remove_user_from_session)(http_request)
            http_request.session.save()
            return OperationSuccessStatus.OPERATION_SUCCESS.value
        else:
            return OperationSuccessStatus.OPERATION_DENIED.value



    async def websocket_logout(self,
                         session_scope: dict) -> PayloadStatusResponse[OperationSuccessResponse]:
        if self.websocket_session_service.user_in_session(session_scope):
            await self.websocket_session_service.remove_user_from_session(session_scope)
            return OperationSuccessStatus.OPERATION_SUCCESS.value
        else:
            return OperationSuccessStatus.OPERATION_DENIED.value

    def get_response(self, payload_status_response: PayloadStatusResponse):
        return Response(payload_status_response.payload,
                        status=payload_status_response.status_code)