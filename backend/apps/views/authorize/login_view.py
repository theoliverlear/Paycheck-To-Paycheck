from kombu.asynchronous.http import Response
from rest_framework.views import APIView

from backend.apps.comm.request.user_request import UserRequest
from backend.apps.comm.response.auth_status import AuthStatus
from backend.apps.comm.serialize.comm.request.user_request_serializer import \
    UserRequestSerializer
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.services.auth_service import AuthService


class LoginView(APIView):
    def __init__(self,
                 auth_service: AuthService):
        super().__init__()
        self.auth_service = auth_service

    def post(self, request, *args, **kwargs):
        serializer: UserRequestSerializer = UserRequestSerializer(data=request.data)
        if serializer.is_valid():
            user_request: UserRequest = serializer.get_instance()
            payload_status: PayloadStatusResponse[AuthStatus] = self.auth_service.login(user_request)
            # TODO: Save user to session
            return Response(payload_status.payload, status=payload_status.status)
        else:
            return Response(serializer.errors, status=400)


