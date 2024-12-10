from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.comm.serialize.comm.request.login_request_serializer import \
    LoginRequestSerializer
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.services.auth_service import AuthService


class LoginView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService):
        super().__init__()
        self.auth_service = auth_service

    def post(self, http_request, *args, **kwargs):
        serializer: LoginRequestSerializer = LoginRequestSerializer(data=http_request.data)
        if serializer.is_valid():
            login_request: LoginRequest = serializer.get_instance()
            payload_status: PayloadStatusResponse[AuthStatusResponse] = self.auth_service.login(login_request, http_request)
            return Response(payload_status.payload,
                            status=payload_status.status_code)
        else:
            return Response(serializer.errors, status=400)


