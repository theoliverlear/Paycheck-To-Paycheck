# paycheck_view.py
import logging
from datetime import date

from asgiref.sync import async_to_sync
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.serialize.entity.paycheck.paycheck_serializer import \
    PaycheckSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.time.date_range import DateRange
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.user.user import User
from backend.apps.models.date_utilities import get_next_week
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.operation_sucess_status import \
    OperationSuccessStatus
from backend.apps.services.auth_service import AuthService
from backend.apps.services.paycheck_service import PaycheckService
from backend.apps.services.session.session_service import SessionService
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
            user: User = await self.session_service.get_user_from_session(http_request)
            logging.info(user)
            paycheck: Paycheck = self.paycheck_service.get_paycheck_from_now(user=user, num_paychecks=paycheck_num)
            # TODO: Refactor this into their respective classes.
            for income in paycheck.recurring_incomes:
                if income.recurring_date.interval == YearInterval.YEARLY:
                    income.amount = income.yearly_income / YearInterval.BI_WEEKLY.value
            for bill in paycheck.recurring_bills:
                if bill.recurring_date.interval == YearInterval.WEEKLY:
                    date_range: DateRange = DateRange(start_date=bill.recurring_date.day, end_date=paycheck.date_range.end_date)
                    next_bill_week: date = get_next_week(date_range.start_date)
                    if date_range.in_range(next_bill_week):
                        bill.amount *= 2

            for wage_income in paycheck.wage_incomes:
                wage_income._amount = wage_income.calculate_paycheck_income()
            paycheck.left_over_income = self.paycheck_service.get_wallet_from_future_paychecks(user, paycheck_num)
            print("Left over income: ", paycheck.left_over_income)
            paycheck_serializer: PaycheckSerializer = PaycheckSerializer(instance=paycheck)
            return Response(paycheck_serializer.data, status=200)
        else:
            serializer: PayloadStatusResponseSerializer = (
                PayloadStatusResponseSerializer(OperationSuccessStatus.OPERATION_DENIED.value))
            return Response(serializer.data, status=401)

    def get(self, http_request, paycheck_num, *args, **kwargs):
        return async_to_sync(self.async_get)(http_request, paycheck_num, *args, **kwargs)




