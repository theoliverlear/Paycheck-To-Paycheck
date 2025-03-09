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

@injectable
class RecurringIncomeConsumer(WebSocketConsumer[RecurringIncome]):
    @inject
    def __init__(self, recurring_income_parser: RecurringIncomeDictParser):
        super().__init__()
        self.recurring_income_parser: RecurringIncomeDictParser = recurring_income_parser

    @override
    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            payload = json.loads(text_data)
            recurring_income: RecurringIncome = self.get_recurring_income(payload)
            recurring_income = await sync_to_async(recurring_income.save)()
            income_json: dict = self.get_serialized_income(recurring_income)
            await self.send(text_data=json.dumps({
                'message': income_json
            }))

    def get_serialized_income(self, recurring_income: RecurringIncome):
        serializer: RecurringIncomeSerializer = RecurringIncomeSerializer(recurring_income)
        return camelize(serializer.data)

    def get_recurring_income(self, json_data):
        return self.recurring_income_parser.get_recurring_income(json_data)