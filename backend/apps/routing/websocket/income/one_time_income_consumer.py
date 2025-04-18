import json

from asgiref.sync import sync_to_async
from djangorestframework_camel_case.util import camelize, underscoreize
from injector import inject

from backend.apps.comm.serialize.entity.income.one_time_income_serializer import \
    OneTimeIncomeSerializer
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.injector.injectable import injectable
from backend.apps.models.dict.entity.income.one_time_income_dict_parser import \
    OneTimeIncomeDictParser
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer
from backend.apps.services.session.websocket_session_service import \
    WebSocketSessionService


@injectable
class OneTimeIncomeConsumer(WebSocketConsumer[OneTimeIncome]):
    @inject
    def __init__(self,
                 one_time_income_parser: OneTimeIncomeDictParser,
                 websocket_session_service: WebSocketSessionService):
        super().__init__()
        self.one_time_income_parser: OneTimeIncomeDictParser = one_time_income_parser
        self.websocket_session_service: WebSocketSessionService = websocket_session_service

    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            payload = json.loads(text_data)
            income: OneTimeIncome = self.get_income(payload)
            income = await self.add_income_to_session_user(income)
            income_json = self.get_serialized_income(income)
            await self.send(text_data=json.dumps({
                'message': income_json
            }))

    async def add_income_to_session_user(self, income: OneTimeIncome):
        from backend.apps.entity.user.user import User
        user: User = await self.websocket_session_service.get_user_from_session(self.scope)
        income.income_history = user.user_income_history
        income = await income.save()
        user.user_income_history.add_one_time_income(income)
        await user.update()
        return income

    def get_serialized_income(self, income: OneTimeIncome):
        serializer: OneTimeIncomeSerializer = OneTimeIncomeSerializer(income)
        return camelize(serializer.data)

    def get_income(self, json_data):
        return self.one_time_income_parser.get_one_time_income(underscoreize(json_data))
