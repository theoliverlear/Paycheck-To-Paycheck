from typing import List

from django.urls import re_path, URLPattern, URLResolver
from injector import Injector

from backend.apps.injector import AppModule
from backend.apps.routing.websocket.bill.bill_consumer import BillConsumer
from backend.apps.routing.websocket.income.income_consumer import \
    IncomeConsumer

injector = Injector(AppModule())

websocket_url_patterns = [
    re_path('ws/bill', BillConsumer.factory(injector)),
    re_path('ws/income', IncomeConsumer.as_asgi())
]
