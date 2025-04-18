from django.urls import re_path
from injector import Injector

from backend.apps.injector import AppModule
from backend.apps.routing.websocket.auth.login_consumer import LoginConsumer
from backend.apps.routing.websocket.auth.signup_consumer import SignupConsumer
from backend.apps.routing.websocket.bill.one_time_bill_consumer import BillConsumer
from backend.apps.routing.websocket.bill.recurring_bill_consumer import \
    RecurringBillConsumer
from backend.apps.routing.websocket.income.recurring_income_consumer import \
    RecurringIncomeConsumer
from backend.apps.routing.websocket.income.one_time_income_consumer import \
    OneTimeIncomeConsumer
from backend.apps.routing.websocket.income.wage_income_consumer import \
    WageIncomeConsumer

injector: Injector = Injector(AppModule())

websocket_url_patterns = [
    re_path('ws/one-time-bill', BillConsumer.factory(injector)),
    re_path('ws/recurring-bill', RecurringBillConsumer.factory(injector)),
    re_path('ws/one-time-income', OneTimeIncomeConsumer.factory(injector)),
    re_path('ws/recurring-income', RecurringIncomeConsumer.factory(injector)),
    re_path('ws/wage-income', WageIncomeConsumer.factory(injector)),
    re_path('ws/signup', SignupConsumer.factory(injector)),
    re_path('ws/login', LoginConsumer.factory(injector))
]
