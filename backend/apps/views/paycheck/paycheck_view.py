# paycheck_view.py
import logging
from datetime import date

from asgiref.sync import async_to_sync
from django.http import HttpResponse
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.serialize.entity.paycheck.paycheck_serializer import \
    PaycheckSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.user.user import User
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.operation_sucess_status import \
    OperationSuccessStatus
from backend.apps.services.auth_service import AuthService
from backend.apps.services.paycheck_service import PaycheckService
from backend.apps.services.session_service import SessionService
from backend.apps.services.user_service import UserService


class PaycheckView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService,
                 user_service: UserService,
                 paycheck_service: PaycheckService,
                 websocket_session_service: SessionService):
        super().__init__()
        self.auth_service: AuthService = auth_service
        self.user_service: UserService = user_service
        self.paycheck_service: PaycheckService = paycheck_service
        self.session_service: SessionService = websocket_session_service

    async def async_get(self, http_request, paycheck_num, *args, **kwargs):
        user_in_session: bool = await self.auth_service.user_in_session(
            communication_type=CommunicationType.HTTP,
            http_request=http_request)
        if user_in_session:
            logging.info(http_request)
            serializer: PayloadStatusResponseSerializer = (
                PayloadStatusResponseSerializer(OperationSuccessStatus.OPERATION_SUCCESS.value))
            user: User = await self.session_service.get_user_from_session(http_request)
            logging.info(user)
            paycheck: Paycheck = self.paycheck_service.get_paycheck_from_now(user=user, num_paychecks=paycheck_num)
            paycheck_serializer: PaycheckSerializer = PaycheckSerializer(instance=paycheck)
            logging.info(paycheck)
            return Response(paycheck_serializer.data, status=200)
        else:
            logging.info("User not in session")
            serializer: PayloadStatusResponseSerializer = (
                PayloadStatusResponseSerializer(OperationSuccessStatus.OPERATION_DENIED.value))
            return Response(serializer.data, status=401)

    def get(self, http_request, paycheck_num, *args, **kwargs):
        return async_to_sync(self.async_get)(http_request, paycheck_num, *args, **kwargs)




