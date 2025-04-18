from typing import override

from injector import Binder, singleton, Module

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.bill.recurring_bill import RecurringBill
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome
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
from backend.apps.repository.bill.one_time_bill_repository import \
    OneTimeBillRepository
from backend.apps.repository.income.income_history_repository import \
    IncomeHistoryRepository
from backend.apps.repository.income.one_time_income_repository import \
    OneTimeIncomeRepository
from backend.apps.repository.user_repository import UserRepository
from backend.apps.repository.wallet_repository import WalletRepository
from backend.apps.services.auth_service import AuthService
from backend.apps.services.bill.one_time_bill_service import \
    OneTimeBillService
from backend.apps.services.income.income_history_service import \
    IncomeHistoryService
from backend.apps.services.income.one_time_income_service import \
    OneTimeIncomeService
from backend.apps.services.paycheck_service import PaycheckService
from backend.apps.services.wallet_service import WalletService
from backend.apps.services.session.websocket_session_service import WebSocketSessionService
from backend.apps.services.user_service import UserService
from backend.apps.repository.income.recurring_income_repository import \
    RecurringIncomeRepository
from backend.apps.repository.income.wage_income_repository import \
    WageIncomeRepository
from backend.apps.repository.bill.bill_history_repository import \
    BillHistoryRepository
from backend.apps.services.income.recurring_income_service import \
    RecurringIncomeService
from backend.apps.services.income.wage_income_service import \
    WageIncomeService
from backend.apps.services.bill.bill_history_service import \
    BillHistoryService
from backend.apps.repository.bill.recurring_bill_repository import \
    RecurringBillRepository
from backend.apps.services.bill.recurring_bill_service import \
    RecurringBillService

class AppModule(Module):
    def __init__(self, *args, **kwargs):
        super().__init__()

    @override
    def configure(self, binder: Binder):

        repositories = [UserRepository, WalletRepository,
                        IncomeHistoryRepository,
                        OneTimeIncomeRepository, RecurringIncomeRepository,
                        WageIncomeRepository, BillHistoryRepository,
                        OneTimeBillRepository, RecurringBillRepository,]

        services = [AuthService, UserService, WalletService,
                    WebSocketSessionService, PaycheckService, IncomeHistoryService,
                    OneTimeIncomeService, RecurringIncomeService, WageIncomeService,
                    BillHistoryService, OneTimeBillService, RecurringBillService,]
        dict_parsers = [DictParser, OneTimeBillDictParser, OneTimeIncomeDictParser,
                        RecurringIncomeDictParser]
        class_parser_targets = [OneTimeBill, OneTimeIncome, RecurringIncome,
                                SignupRequest, LoginRequest, RecurringBill,
                                WageIncome]
        self.simple_bind(ClassFieldParser, binder)

        self.simple_bind_all(repositories, binder)
        self.simple_bind_all(services, binder)
        self.simple_bind_all(dict_parsers, binder)
        self.bind_all_class_parsers(class_parser_targets, binder)


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