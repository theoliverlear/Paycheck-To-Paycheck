import json
import logging
from datetime import date

from asgiref.sync import sync_to_async

from backend.apps.comm.serialize.entity.bill.bill_serializer import \
    BillSerializer
from backend.apps.entity.bill.bill import Bill
from backend.apps.entity.time.due_date import DueDate
from backend.apps.models.date_utilities import iso_to_django_date
from backend.apps.routing.websocket.websocket_consumer import \
    WebSocketConsumer


class BillConsumer(WebSocketConsumer[Bill]):
    async def connect(self):
        logging.info('WebSocket connected')
        await self.accept()

    async def disconnect(self, close_code):
        logging.info('WebSocket disconnected')

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            logging.info(f"Received text data: {text_data}")
            data = json.loads(text_data)
            bill: Bill = self.get_bill(data)
            await sync_to_async(bill.save)()
            bill_json = self.get_bill_from_json(data)
            await self.send(text_data=json.dumps({
                'message': bill_json
            }))

    def get_bill_from_json(self, json_data):
        json_bill = self.get_bill(json_data)
        # TODO: See if bill already exists or not and implement ID
        #       accordingly.
        serializer: BillSerializer = BillSerializer(json_bill)
        return serializer.data
        # return json_bill.model_dump_json()

    def get_bill(self, json_data):
        json_date: date = iso_to_django_date(json_data['date'])
        json_due_date = DueDate(due_date=json_date)
        bill: Bill = Bill(
            name=json_data['title'],
            amount=json_data['amount'],
            due_date=json_due_date
        )
        return bill

