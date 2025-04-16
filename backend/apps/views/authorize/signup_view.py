# signup_view.py
from asgiref.sync import async_to_sync
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.comm.serialize.comm.request.signup_request_serializer import \
    SignupRequestSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.models.dict.comm.request.signup_request_dict_parser import \
    SignupRequestDictParser
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.services.auth_service import AuthService


class SignupView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService,
                 dict_parser: SignupRequestDictParser):
        super().__init__()
        self.auth_service = auth_service
        self.dict_parser: SignupRequestDictParser = dict_parser
    async def async_post(self, http_request, *args, **kwargs):
        signup_request = self.dict_parser.get_signup_request(http_request.data)
        payload_status: PayloadStatusResponse[AuthStatusResponse] = \
            await self.auth_service.signup(signup_request, http_request)
        payload_status_serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(payload_status)
        return Response(payload_status_serializer.data,
                        status=payload_status.status_code)

    def post(self, request, *args, **kwargs):
        return async_to_sync(self.async_post)(request, *args, **kwargs)