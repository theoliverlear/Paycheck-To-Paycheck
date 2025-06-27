from asgiref.sync import async_to_sync
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.response.income_response import IncomesResponse
from backend.apps.comm.serialize.comm.response.incomes_response_serializer import \
    IncomesResponseSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.entity.user.user import User
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.operation_sucess_status import \
    OperationSuccessStatus
from backend.apps.services.auth_service import AuthService
from backend.apps.services.session.session_service import SessionService


class GetAllIncomesView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService,
                 session_service: SessionService):
        super().__init__()
        self.auth_service: AuthService = auth_service
        self.session_service: SessionService = session_service

    async def async_get(self, http_request, *args, **kwargs):
        user_in_session: bool = await self.auth_service.user_in_session(
            communication_type=CommunicationType.HTTP,
            http_request=http_request
        )
        if user_in_session:
            user: User = await self.session_service.get_user_from_session(http_request)
            for wage_income in user.user_income_history.wage_incomes:
                wage_income.amount = wage_income.calculate_paycheck_income()
            incomes_response: IncomesResponse = IncomesResponse(
                one_time_incomes=user.user_income_history.one_time_incomes,
                recurring_incomes=user.user_income_history.recurring_incomes,
                wage_incomes=user.user_income_history.wage_incomes
            )
            serializer: IncomesResponseSerializer = IncomesResponseSerializer(incomes_response)
            return Response(serializer.data, status=200)
        else:
            serializer: PayloadStatusResponseSerializer = (
                PayloadStatusResponseSerializer(OperationSuccessStatus.OPERATION_DENIED.value))
            return Response(serializer.data, status=401)

    def get(self, http_request, *args, **kwargs):
        return async_to_sync(self.async_get)(http_request, *args, **kwargs)