# is_logged_in_view.py
from asgiref.sync import async_to_sync
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.services.auth_service import AuthService


class IsLoggedInView(APIView):
    @inject
    def __init__(self, auth_service: AuthService):
        super().__init__()
        self.auth_service: AuthService = auth_service

    async def async_get(self, http_request, *args, **kwargs):
        payload_status: PayloadStatusResponse[AuthStatusResponse] = (
            await self.auth_service.is_logged_in(CommunicationType.HTTP, http_request=http_request))
        print(payload_status)
        serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(payload_status)
        response = Response(serializer.data)
        # TODO: Find a way to remove this boilerplate.
        response['Access-Control-Allow-Origin'] = 'http://localhost:4200'
        response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'

        return response

    def get(self, http_request, *args, **kwargs):
        return async_to_sync(self.async_get)(http_request, *args, **kwargs)
