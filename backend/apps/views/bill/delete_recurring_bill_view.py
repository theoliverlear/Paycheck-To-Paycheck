from asgiref.sync import async_to_sync
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.entity.user.user import User
from backend.apps.models.dict.entity.bill.recurring_bill_dict_parser import \
    RecurringBillDictParser
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.operation_sucess_status import \
    OperationSuccessStatus
from backend.apps.services.auth_service import AuthService
from backend.apps.services.bill.recurring_bill_service import \
    RecurringBillService
from backend.apps.services.session.session_service import SessionService


class DeleteRecurringBillView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService,
                 session_service: SessionService,
                 recurring_bill_service: RecurringBillService,
                 recurring_bill_dict_parser: RecurringBillDictParser):
        super().__init__()
        self.auth_service: AuthService = auth_service
        self.session_service: SessionService = session_service
        self.recurring_bill_service: RecurringBillService = recurring_bill_service
        self.recurring_bill_dict_parser: RecurringBillDictParser = \
            recurring_bill_dict_parser

    async def async_delete(self, http_request, bill_id: int, *args, **kwargs):
        user_in_session: bool = await self.auth_service.user_in_session(
            communication_type=CommunicationType.HTTP,
            http_request=http_request
        )
        if user_in_session:
            user: User = await self.session_service.get_user_from_session(http_request)
            await self.recurring_bill_service.delete_from_user(user, bill_id)
            serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(
                OperationSuccessStatus.OPERATION_SUCCESS.value
            )
            return Response(status=200, data=serializer.data)
        else:
            serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(
                OperationSuccessStatus.OPERATION_DENIED.value
            )
            return Response(status=401, data=serializer.data)

    def delete(self, http_request, bill_id, *args, **kwargs):
        return async_to_sync(self.async_delete)(http_request, bill_id, *args, **kwargs)