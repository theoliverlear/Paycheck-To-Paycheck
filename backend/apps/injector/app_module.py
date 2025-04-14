from typing import override

from injector import Binder, singleton, Module

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.class_field_parser_provider import \
    ClassDictParserProvider
from backend.apps.models.dict.dict_parser import DictParser
from backend.apps.models.dict.entity.bill.one_time_bill_dict_parser import \
    OneTimeBillDictParser
from backend.apps.models.dict.entity.income.one_time_income_dict_parser import \
    OneTimeIncomeDictParser
from backend.apps.models.dict.entity.income.recurring_income_dict_parser import \
    RecurringIncomeDictParser
from backend.apps.repository.user_repository import UserRepository
from backend.apps.repository.wallet_repository import WalletRepository
from backend.apps.routing.websocket.bill.one_time_bill_consumer import BillConsumer
from backend.apps.services.auth_service import AuthService
from backend.apps.services.paycheck_service import PaycheckService
from backend.apps.services.wallet_service import WalletService
from backend.apps.services.websocket_session_service import WebSocketSessionService
from backend.apps.services.user_service import UserService

class AppModule(Module):
    def __init__(self, *args, **kwargs):
        super().__init__()

    @override
    def configure(self, binder: Binder):
        repositories = [UserRepository, WalletRepository]
        services = [AuthService, UserService, WalletService,
                    WebSocketSessionService, PaycheckService]
        dict_parsers = [DictParser, OneTimeBillDictParser, OneTimeIncomeDictParser,
                        RecurringIncomeDictParser]
        class_parser_targets = [OneTimeBill, OneTimeIncome, RecurringIncome,
                                SignupRequest, LoginRequest]
        self.simple_bind(ClassFieldParser, binder)

        self.simple_bind_all(repositories, binder)
        self.simple_bind_all(services, binder)
        self.simple_bind_all(dict_parsers, binder)
        self.bind_all_class_parsers(class_parser_targets, binder)

        # binder.bind(ClassFieldParser, to=ClassFieldParser, scope=singleton)
        # binder.bind(UserRepository, to=UserRepository, scope=singleton)
        # binder.bind(WalletRepository, to=WalletRepository, scope=singleton)

        # binder.bind(UserService, to=UserService, scope=singleton)
        # binder.bind(AuthService, to=AuthService, scope=singleton)

        # binder.bind(BillConsumer, to=BillConsumer, scope=singleton)
        # binder.bind(WebSocketSessionService, to=WebSocketSessionService, scope=singleton)

        # binder.bind(DictParser, to=DictParser, scope=singleton)
        # binder.bind(OneTimeBillDictParser, to=OneTimeBillDictParser, scope=singleton)
        # binder.bind(OneTimeIncomeDictParser, to=OneTimeIncomeDictParser, scope=singleton)
        # binder.bind(RecurringIncomeDictParser, to=RecurringIncomeDictParser, scope=singleton)

        # binder.bind(ClassFieldParser[OneTimeBill], to=ClassDictParserProvider(OneTimeBill), scope=singleton)
        # binder.bind(ClassFieldParser[OneTimeIncome], to=ClassDictParserProvider(OneTimeIncome), scope=singleton)
        # binder.bind(ClassFieldParser[RecurringIncome], to=ClassDictParserProvider(RecurringIncome), scope=singleton)
        # binder.bind(ClassFieldParser[SignupRequest], to=ClassDictParserProvider(SignupRequest), scope=singleton)
        # binder.bind(ClassFieldParser[LoginRequest], to=ClassDictParserProvider(LoginRequest), scope=singleton)



    def bind_all_class_parsers(self, classes_bound, binder: Binder):
        for class_bound in classes_bound:
            self.bind_class_parser(class_bound, binder)

    def bind_class_parser(self, class_bound, binder: Binder):
        binder.bind(ClassFieldParser[class_bound], to=ClassDictParserProvider(class_bound), scope=singleton)

    def simple_bind_all(self, class_references, binder: Binder):
        for class_reference in class_references:
            self.simple_bind(class_reference, binder)

    def simple_bind(self, class_reference,
                    binder: Binder):
        binder.bind(class_reference, to=class_reference, scope=singleton)