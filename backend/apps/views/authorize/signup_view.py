from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.serialize.comm.request.signup_request_serializer import \
    SignupRequestSerializer
from backend.apps.services.auth_service import AuthService


class SignupView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService):
        super().__init__()
        self.auth_service = auth_service
    async def post(self, http_request, *args, **kwargs):
        serializer: SignupRequestSerializer = SignupRequestSerializer(data=http_request.data)
        if serializer.is_valid():
            signup_request = serializer.get_instance()
            payload_status = await self.auth_service.signup(signup_request, http_request)
            return Response(payload_status.payload,
                            status=payload_status.status_code)
        else:
            return Response(serializer.errors, status=400)
