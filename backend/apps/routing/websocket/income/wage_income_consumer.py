from typing import override
from djangorestframework_camel_case.util import camelize
from injector import inject

from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.injector.injectable import injectable
from backend.apps.models.dict.entity.income.wage_income_dict_parser import \
    WageIncomeDictParser
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer
from backend.apps.services.session.websocket_session_service import \
    WebSocketSessionService


@injectable
class WageIncomeConsumer(WebSocketConsumer[WageIncome]):
    @inject
    def __init__(self,
                 wage_income_dict_parser: WageIncomeDictParser,
                 websocket_session_service: WebSocketSessionService):
        super().__init__()
        self.wage_income_dict_parser: WageIncomeDictParser = wage_income_dict_parser
        self.websocket_session_service: WebSocketSessionService = websocket_session_service

    @override
    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            import json
            payload = json.loads(text_data)
            income: WageIncome = self.get_wage_income(payload)
            income = await self.add_income_to_session_user(income)
            income_json: dict = self.get_serialized_wage_income(income)
            await self.send(text_data=json.dumps({
                'message': income_json
            }))

    async def add_income_to_session_user(self, income: WageIncome):
        from backend.apps.entity.user.user import User
        user: User = await self.websocket_session_service.get_user_from_session(self.scope)
        income.income_history = user.user_income_history
        income = await income.save()
        user.user_income_history.add_wage_income(income)
        await user.update()
        return income

    def get_wage_income(self, json_data):
        return self.wage_income_dict_parser.get_wage_income(json_data)

    def get_serialized_wage_income(self, wage_income: WageIncome):
        from backend.apps.comm.serialize.entity.income.wage_income_serializer import \
            WageIncomeSerializer
        serializer: WageIncomeSerializer = WageIncomeSerializer(wage_income)
        return camelize(serializer.data)
