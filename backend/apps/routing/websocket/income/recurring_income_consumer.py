import json
from typing import override

from asgiref.sync import sync_to_async
from djangorestframework_camel_case.util import camelize
from injector import inject

from backend.apps.comm.serialize.entity.income.recurring_income_serializer import \
    RecurringIncomeSerializer
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.injector.injectable import injectable
from backend.apps.models.dict.entity.income.recurring_income_dict_parser import \
    RecurringIncomeDictParser
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer
from backend.apps.services.session.websocket_session_service import \
    WebSocketSessionService


@injectable
class RecurringIncomeConsumer(WebSocketConsumer[RecurringIncome]):
    @inject
    def __init__(self,
                 recurring_income_parser: RecurringIncomeDictParser,
                 websocket_session_service: WebSocketSessionService):
        super().__init__()
        self.recurring_income_parser: RecurringIncomeDictParser = recurring_income_parser
        self.websocket_session_service: WebSocketSessionService = websocket_session_service

    @override
    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            payload = json.loads(text_data)
            recurring_income: RecurringIncome = self.get_recurring_income(payload)
            recurring_income = await self.add_recurring_income_to_session_user(recurring_income)
            income_json: dict = self.get_serialized_income(recurring_income)
            await self.send(text_data=json.dumps({
                'message': income_json
            }))

    async def add_recurring_income_to_session_user(self, income: RecurringIncome):
        from backend.apps.entity.user.user import User
        user: User = await self.websocket_session_service.get_user_from_session(self.scope)
        income.income_history = user.user_income_history
        income = await sync_to_async(income.save)()
        user.user_income_history.add_recurring_income(income)
        await user.update()
        return income

    def get_serialized_income(self, recurring_income: RecurringIncome):
        serializer: RecurringIncomeSerializer = RecurringIncomeSerializer(recurring_income)
        return camelize(serializer.data)

    def get_recurring_income(self, json_data):
        return self.recurring_income_parser.get_recurring_income(json_data)