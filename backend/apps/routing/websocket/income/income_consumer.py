import json

from asgiref.sync import sync_to_async

from backend.apps.comm.serialize.entity.income.one_time_income_serializer import \
    IncomeSerializer
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer


class IncomeConsumer(WebSocketConsumer[OneTimeIncome]):
    async def receive(self, text_data=None, bytes_data=None) -> None:
        if text_data:
            data = json.loads(text_data)
            income: OneTimeIncome = self.get_income(data)
            await sync_to_async(income.save)()
            income_json = self.get_income_from_json(data)
            await self.send(text_data=json.dumps({
                'message': income_json
            }))

    def get_income_from_json(self, json_data):
        json_income = self.get_income(json_data)
        serializer: IncomeSerializer = IncomeSerializer(json_income)
        return serializer.data

    def get_income(self, json_data):
        json_name = json_data['title']
        json_income_amount = json_data['amount']
        income: OneTimeIncome = OneTimeIncome(
            name=json_name,
            income_amount=json_income_amount
        )
        return income
