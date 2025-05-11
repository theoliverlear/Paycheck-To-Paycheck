from asgiref.sync import async_to_sync
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.entity.user.user import User
from backend.apps.models.dict.entity.income.one_time_income_dict_parser import \
    OneTimeIncomeDictParser
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.operation_sucess_status import \
    OperationSuccessStatus
from backend.apps.services.auth_service import AuthService
from backend.apps.services.income.one_time_income_service import \
    OneTimeIncomeService
from backend.apps.services.session.session_service import SessionService


class DeleteOneTimeIncomeView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService,
                 session_service: SessionService,
                 one_time_income_service: OneTimeIncomeService,
                 one_time_income_dict_parser: OneTimeIncomeDictParser):
        super().__init__()
        self.auth_service: AuthService = auth_service
        self.session_service: SessionService = session_service
        self.one_time_income_service: OneTimeIncomeService = one_time_income_service
        self.one_time_income_dict_parser: OneTimeIncomeDictParser = one_time_income_dict_parser

    async def async_delete(self, http_request, income_id: int, *args, **kwargs):
        user_in_session: bool = await self.auth_service.user_in_session(
            communication_type=CommunicationType.HTTP,
            http_request=http_request
        )
        if user_in_session:
            user: User = await self.session_service.get_user_from_session(http_request)
            await self.one_time_income_service.delete_from_user(user, income_id)
            serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(
                OperationSuccessStatus.OPERATION_SUCCESS.value
            )
            return Response(status=200, data=serializer.data)
        else:
            serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(
                OperationSuccessStatus.OPERATION_DENIED.value
            )
            return Response(status=401, data=serializer.data)

    def delete(self, http_request, income_id, *args, **kwargs):
        return async_to_sync(self.async_delete)(http_request, income_id, *args, **kwargs)