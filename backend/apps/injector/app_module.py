from typing import override

from injector import Binder, singleton, Module

from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.class_field_parser_provider import \
    ClassDictParserProvider
from backend.apps.models.dict.dict_parser import DictParser
from backend.apps.models.dict.entity.bill.one_time_bill_dict_parser import \
    OneTimeBillDictParser
from backend.apps.repository.user_repository import UserRepository
from backend.apps.routing.websocket.bill.bill_consumer import BillConsumer
from backend.apps.services.auth_service import AuthService
from backend.apps.services.websocket_session_service import WebSocketSessionService
from backend.apps.services.user_service import UserService

class AppModule(Module):
    def __init__(self, *args, **kwargs):
        super().__init__()

    @override
    def configure(self, binder: Binder):
        binder.bind(UserRepository, to=UserRepository, scope=singleton)
        binder.bind(UserService, to=UserService, scope=singleton)
        binder.bind(AuthService, to=AuthService, scope=singleton)

        binder.bind(BillConsumer, to=BillConsumer, scope=singleton)

        binder.bind(DictParser, to=DictParser, scope=singleton)
        binder.bind(OneTimeBillDictParser, to=OneTimeBillDictParser, scope=singleton)

        binder.bind(ClassFieldParser, to=ClassFieldParser, scope=singleton)
        binder.bind(ClassFieldParser[OneTimeBill], to=ClassDictParserProvider(OneTimeBill), scope=singleton)
        binder.bind(ClassFieldParser[SignupRequest], to=ClassDictParserProvider(SignupRequest), scope=singleton)

        binder.bind(WebSocketSessionService, to=WebSocketSessionService, scope=singleton)
        # self.bind_dict_parsers(binder)
        # self.bind_class_dict_parsers(binder)



    # def bind_dict_parsers(self, binder: Binder):
    #     binder.bind(DictParser, to=DictParser, scope=singleton)
    #     dict_parsers = [OneTimeBillDictParser]
    #     for dict_parser in dict_parsers:
    #         binder.bind(dict_parser, to=dict_parser, scope=singleton)
    #
    #
    # def bind_class_dict_parsers(self, binder: Binder):
    #     binder.bind(ClassDictParser, to=ClassDictParser, scope=singleton)
    #     parsable_classes = [OneTimeBill]
    #     for parsable_class in parsable_classes:
    #         binder.bind(ClassDictParser[parsable_class], to=ClassDictParser(parsable_class), scope=singleton)