from asgiref.sync import async_to_sync
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.response.completed_welcome_response import \
    CompletedWelcomeResponse
from backend.apps.comm.serialize.comm.response.completed_welcome_response_serializer import \
    CompletedWelcomeResponseSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.operation_sucess_status import \
    OperationSuccessStatus
from backend.apps.services.auth_service import AuthService
from backend.apps.services.session.session_service import SessionService


class HasCompletedWelcomeView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService,
                 session_service: SessionService):
        super().__init__()
        self.auth_service: AuthService = auth_service
        self.session_service: SessionService = session_service

    async def async_get(self, http_request, *args, **kwargs):
        user_in_session: bool = await self.auth_service.user_in_session(
            communication_type=CommunicationType.HTTP,
            http_request=http_request
        )
        if user_in_session:
            user = await self.session_service.get_user_from_session(http_request)
            has_completed_welcome: CompletedWelcomeResponse = CompletedWelcomeResponse(user.completed_welcome)
            serializer: CompletedWelcomeResponseSerializer = CompletedWelcomeResponseSerializer(has_completed_welcome)
            return Response(status=200, data=serializer.data)
        else:
            serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(
                OperationSuccessStatus.OPERATION_DENIED.value
            )
            return Response(status=401, data=serializer.data)

    def get(self, http_request, *args, **kwargs):
        return async_to_sync(self.async_get)(http_request, *args, **kwargs)