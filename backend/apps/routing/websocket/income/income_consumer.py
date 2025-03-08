import json
import logging

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

@injectable
class IncomeConsumer(WebSocketConsumer[OneTimeIncome]):
    @inject
    def __init__(self, one_time_income_parser: OneTimeIncomeDictParser):
        super().__init__()
        self.one_time_income_parser: OneTimeIncomeDictParser = one_time_income_parser

    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            data = json.loads(text_data)
            income: OneTimeIncome = self.get_income(data)
            await sync_to_async(income.save)()
            income_json = self.get_serialized_income(income)
            await self.send(text_data=json.dumps({
                'message': income_json
            }))

    def get_serialized_income(self, income: OneTimeIncome):
        serializer: OneTimeIncomeSerializer = OneTimeIncomeSerializer(income)
        return camelize(serializer.data)

    def get_income(self, json_data):
        return self.one_time_income_parser.get_one_time_income(underscoreize(json_data))
