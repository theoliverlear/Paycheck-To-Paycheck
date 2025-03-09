import json
import logging
from typing import override

from asgiref.sync import sync_to_async
from djangorestframework_camel_case.util import camelize
from injector import inject, Injector

from backend.apps.comm.serialize.entity.bill.one_time_bill_serializer import \
    OneTimeBillSerializer
from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.injector.injectable import injectable
from backend.apps.models.dict.entity.bill.one_time_bill_dict_parser import \
    OneTimeBillDictParser
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer

@injectable
class BillConsumer(WebSocketConsumer[OneTimeBill]):
    @inject
    def __init__(self, one_time_bill_parser: OneTimeBillDictParser):
        super().__init__()
        self.one_time_bill_parser: OneTimeBillDictParser = one_time_bill_parser

    @override
    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            logging.info(f"Received text data: {text_data}")
            payload = json.loads(text_data)
            bill: OneTimeBill = self.get_bill(payload)
            bill = await sync_to_async(bill.save)()
            bill_json: dict = self.get_serialized_bill(bill)
            await self.send(text_data=json.dumps({
                'message': bill_json
            }))

    def get_serialized_bill(self, bill: OneTimeBill) -> dict:
        serializer: OneTimeBillSerializer = OneTimeBillSerializer(bill)
        return camelize(serializer.data)

    def get_bill(self, json_data):
        return self.one_time_bill_parser.get_one_time_bill(json_data)

