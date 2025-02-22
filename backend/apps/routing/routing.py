from django.urls import re_path

from backend.apps.routing.websocket.bill.bill_consumer import BillConsumer

websocket_url_patterns = [
    re_path('ws/bill', BillConsumer.as_asgi())
]
