import json
import logging
from typing import override

from injector import inject

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.comm.serialize.comm.request.login_request_serializer import \
    LoginRequestSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.injector.injectable import injectable
from backend.apps.models.dict.comm.request.login_request_dict_parser import \
    LoginRequestDictParser
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer
from backend.apps.services.auth_service import AuthService


@injectable
class LoginConsumer(WebSocketConsumer[LoginRequest]):
    @inject
    def __init__(self,
                 auth_service: AuthService,
                 login_request_parser: LoginRequestDictParser):
        super().__init__()
        self.auth_service: AuthService = auth_service
        self.login_request_parser: LoginRequestDictParser = login_request_parser

    @override
    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            logging.info(f"Received text data: {text_data}")
            json_data = json.loads(text_data)
            login_request: LoginRequest = self.get_login_request(json_data)
            payload_response: PayloadStatusResponse[AuthStatusResponse] = await self.auth_service.websocket_login(login_request, self.scope)
            await self.send(
                text_data=json.dumps({
                'message': self.get_serialized_payload_status_response(payload_response)
            }))

    def get_serialized_payload_status_response(self,
                                               payload_status_response: PayloadStatusResponse[AuthStatusResponse]):
        serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(payload_status_response)
        serialized_response = serializer.data
        return serialized_response

    def get_serialized_login_request(self, login_request: LoginRequest):
        serializer: LoginRequestSerializer = LoginRequestSerializer(login_request)
        return serializer.data

    def get_login_request(self, json_data):
        return self.login_request_parser.get_login_request(json_data)
