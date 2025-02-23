from typing import List

from django.urls import re_path, URLPattern, URLResolver

from backend.apps.routing.websocket.bill.bill_consumer import BillConsumer
from backend.apps.routing.websocket.income.income_consumer import \
    IncomeConsumer

websocket_url_patterns = [
    re_path('ws/bill', BillConsumer.as_asgi()),
    re_path('ws/income', IncomeConsumer.as_asgi())
]
