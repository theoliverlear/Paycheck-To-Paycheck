import json
import logging
from typing import override

from djangorestframework_camel_case.util import camelize
from injector import inject

from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.comm.serialize.comm.request.signup_request_serializer import \
    SignupRequestSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.injector.injectable import injectable
from backend.apps.models.dict.comm.request.signup_request_dict_parser import \
    SignupRequestDictParser
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer
from backend.apps.services.auth_service import AuthService

@injectable
class SignupConsumer(WebSocketConsumer[SignupRequest]):
    @inject
    def __init__(self,
                 signup_request_parser: SignupRequestDictParser,
                 auth_service: AuthService):
        super().__init__()
        self.signup_request_parser: SignupRequestDictParser = signup_request_parser
        self.auth_service: AuthService = auth_service

    @override
    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            logging.info(f"Received text data: {text_data}")
            payload = json.loads(text_data)
            signup_request: SignupRequest = self.get_signup_request(payload)
            payload_response: PayloadStatusResponse[AuthStatusResponse] = await self.auth_service.websocket_signup(signup_request, self.scope)
            await self.send(
                text_data=json.dumps({
                    'message': self.get_serialized_payload_status_response(payload_response)
            }))

    def get_serialized_payload_status_response(self, payload_status_response: PayloadStatusResponse[AuthStatusResponse]):
        serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(payload_status_response)
        serialized_response = serializer.data
        print('serialized data: ', serialized_response)
        return camelize(serialized_response)

    def get_serialized_signup_request(self, signup_request: SignupRequest) -> dict:
        serializer: SignupRequestSerializer = SignupRequestSerializer(signup_request)
        return serializer.data

    def get_signup_request(self, json_data):
        return self.signup_request_parser.get_signup_request(json_data)