from asgiref.sync import async_to_sync
from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.response.operation_success_response import \
    OperationSuccessResponse
from backend.apps.comm.serialize.comm.response.operation_success_response_serializer import \
    OperationSuccessResponseSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.entity.holding.saving.saving import Saving
from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.user.user import User
from backend.apps.entity.wallet.wallet import Wallet
from backend.apps.models.dict.models.welcome.welcome_survey_dict_parser import \
    WelcomeSurveyDictParser
from backend.apps.models.http.communication_type import CommunicationType
from backend.apps.models.http.operation_sucess_status import \
    OperationSuccessStatus
from backend.apps.models.welcome.welcome_survey import WelcomeSurvey
from backend.apps.services.auth_service import AuthService
from backend.apps.services.session.session_service import SessionService


class WelcomeSurveyView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService,
                 session_service: SessionService,
                 welcome_survey_dict_parser: WelcomeSurveyDictParser):
        super().__init__()
        self.auth_service: AuthService = auth_service
        self.session_service: SessionService = session_service
        self.welcome_survey_dict_parser: WelcomeSurveyDictParser = welcome_survey_dict_parser

    async def async_post(self, http_request, *args, **kwargs):
        user_in_session: bool = await self.auth_service.user_in_session(
            communication_type=CommunicationType.HTTP,
            http_request=http_request
        )
        if user_in_session:
            # TODO: Unit test to remove unnecessary persistence.
            user: User = await self.session_service.get_user_from_session(http_request)
            welcome_survey: WelcomeSurvey = self.welcome_survey_dict_parser.get_welcome_survey(http_request.data)
            user.completed_welcome = True
            user.payday = RecurringDate(day=welcome_survey.last_paycheck_date,
                                        interval=YearInterval.BI_WEEKLY)
            user.wallet = Wallet()
            amount_in_wallet = welcome_survey.checking_account_amount - welcome_survey.paycheck_amount
            user.wallet.checking_account = Saving(name='Checking',
                                                  amount=amount_in_wallet,
                                                  wallet=user.wallet)
            await user.wallet.save()
            user.user_income_history = IncomeHistory()
            await user.user_income_history.save()
            paycheck_income: RecurringIncome = RecurringIncome(recurring_date=user.payday,
                                                               name='Job',
                                                               income_history=user.user_income_history,
                                                               amount=welcome_survey.paycheck_amount)
            paycheck_income = await paycheck_income.save()
            user.user_income_history.add_recurring_income(paycheck_income)
            await user.user_income_history.update()
            paycheck_income.income_history = user.user_income_history
            await paycheck_income.save()

            await user.save()
            serializer: OperationSuccessResponseSerializer = OperationSuccessResponseSerializer(
                OperationSuccessResponse(True)
            )
            return Response(status=200, data=serializer.data)
        else:
            serializer: OperationSuccessResponseSerializer = OperationSuccessResponseSerializer(
                OperationSuccessResponse(False)
            )
            return Response(status=401, data=serializer.data)

    def post(self, http_request, *args, **kwargs):
        return async_to_sync(self.async_post)(http_request, *args, **kwargs)