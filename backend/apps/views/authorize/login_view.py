# login_view.py
from asgiref.sync import async_to_sync
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.comm.serialize.comm.request.login_request_serializer import \
    LoginRequestSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.models.dict.comm.request.login_request_dict_parser import \
    LoginRequestDictParser
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.services.auth_service import AuthService


class LoginView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService,
                 dict_parser: LoginRequestDictParser):
        super().__init__()
        self.auth_service: AuthService = auth_service
        self.dict_parser: LoginRequestDictParser = dict_parser

    async def async_post(self, http_request, *args, **kwargs):
        login_request: LoginRequest = self.dict_parser.get_login_request(http_request.data)
        response: PayloadStatusResponse[AuthStatusResponse] = await self.auth_service.http_login(login_request=login_request, http_request=http_request)
        response_serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(response)
        return Response(response_serializer.data, status=response.status_code)


    def post(self, http_request, *args, **kwargs):
        return async_to_sync(self.async_post)(http_request, *args, **kwargs)


