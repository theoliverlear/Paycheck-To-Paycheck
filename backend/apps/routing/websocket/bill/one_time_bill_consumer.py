import json
import logging
from typing import override

from asgiref.sync import sync_to_async
from djangorestframework_camel_case.util import camelize
from injector import inject

from backend.apps.comm.serialize.entity.bill.one_time_bill_serializer import \
    OneTimeBillSerializer
from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.injector.injectable import injectable
from backend.apps.models.dict.entity.bill.one_time_bill_dict_parser import \
    OneTimeBillDictParser
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer
from backend.apps.services.session.websocket_session_service import \
    WebSocketSessionService


@injectable
class BillConsumer(WebSocketConsumer[OneTimeBill]):
    @inject
    def __init__(self,
                 one_time_bill_parser: OneTimeBillDictParser,
                 websocket_session_service: WebSocketSessionService):
        super().__init__()
        self.one_time_bill_parser: OneTimeBillDictParser = one_time_bill_parser
        self.websocket_session_service: WebSocketSessionService = websocket_session_service

    @override
    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            logging.info(f"Received text data: {text_data}")
            payload = json.loads(text_data)
            bill: OneTimeBill = self.get_bill(payload)
            bill = await self.add_bill_to_session_user(bill)
            bill_json: dict = self.get_serialized_bill(bill)
            await self.send(text_data=json.dumps({
                'message': bill_json
            }))

    async def add_bill_to_session_user(self, bill: OneTimeBill):
        from backend.apps.entity.user.user import User
        user: User = await self.websocket_session_service.get_user_from_session(self.scope)
        bill.bill_history = user.user_bill_history
        bill = await bill.save()
        user.user_bill_history.add_one_time_bill(bill)
        print(user)
        await user.update()
        print(Paycheck.from_user(user))
        return bill


    def get_serialized_bill(self, bill: OneTimeBill) -> dict:
        serializer: OneTimeBillSerializer = OneTimeBillSerializer(bill)
        return camelize(serializer.data)

    def get_bill(self, json_data: dict) -> OneTimeBill:
        return self.one_time_bill_parser.get_one_time_bill(json_data)

