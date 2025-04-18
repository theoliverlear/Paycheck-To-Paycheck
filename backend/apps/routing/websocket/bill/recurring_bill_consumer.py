import json
from typing import override

from djangorestframework_camel_case.util import camelize
from injector import inject

from backend.apps.entity.bill.recurring_bill import RecurringBill
from backend.apps.injector.injectable import injectable
from backend.apps.models.dict.entity.bill.recurring_bill_dict_parser import \
    RecurringBillDictParser
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer
from backend.apps.services.session.websocket_session_service import \
    WebSocketSessionService


@injectable
class RecurringBillConsumer(WebSocketConsumer[RecurringBill]):
    @inject
    def __init__(self,
                 recurring_bill_dict_parser: RecurringBillDictParser,
                 websocket_session_service: WebSocketSessionService):
        super().__init__()
        self.recurring_bill_dict_parser: RecurringBillDictParser = recurring_bill_dict_parser
        self.websocket_session_service: WebSocketSessionService = websocket_session_service

    @override
    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            payload = json.loads(text_data)
            bill: RecurringBill = self.get_bill(payload)
            bill = await self.add_bill_to_session_user(bill)
            bill_json: dict = self.get_serialized_bill(bill)
            await self.send(text_data=json.dumps({
                'message': bill_json
            }))


    async def add_bill_to_session_user(self, bill: RecurringBill):
        from backend.apps.entity.user.user import User
        user: User = await self.websocket_session_service.get_user_from_session(self.scope)
        bill.bill_history = user.user_bill_history
        bill = await bill.save()
        user.user_bill_history.add_recurring_bill(bill)
        await user.update()
        return bill

    def get_serialized_bill(self, bill: RecurringBill) -> dict:
        from backend.apps.comm.serialize.entity.bill.recurring_bill_serializer import \
            RecurringBillSerializer
        serializer: RecurringBillSerializer = RecurringBillSerializer(bill)
        return camelize(serializer.data)

    def get_bill(self, json_data) -> RecurringBill:
        return self.recurring_bill_dict_parser.get_recurring_bill(json_data)