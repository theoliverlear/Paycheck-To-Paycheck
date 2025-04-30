from asgiref.sync import async_to_sync
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.response.operation_success_response import \
    OperationSuccessResponse
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse
from backend.apps.services.auth_service import AuthService


class LogoutView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService):
        super().__init__()
        self.auth_service: AuthService = auth_service

    async def async_get(self, http_request, *args, **kwargs):
        payload_status: PayloadStatusResponse[OperationSuccessResponse] = await self.auth_service.logout(CommunicationType.HTTP,
                                                                                                   http_request=http_request)
        serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(payload_status)
        return Response(serializer.data)

    @method_decorator(never_cache)
    def get(self, http_request, *args, **kwargs):

        response: Response = async_to_sync(self.async_get)(http_request, *args, **kwargs)
        response.delete_cookie('devsessionid',
        path = '/',
        domain = None)
        response.delete_cookie('sessionid')
        return response