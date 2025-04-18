# user_service.py
from channels.db import database_sync_to_async
from injector import inject

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.bill.models import BillHistoryOrmModel, \
    OneTimeBillOrmModel, RecurringBillOrmModel
from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.models import IncomeHistoryOrmModel, \
    OneTimeIncomeOrmModel, RecurringIncomeOrmModel, WageIncomeOrmModel
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.entity.user.user import User
from backend.apps.repository.user_repository import UserRepository
from backend.apps.services.bill.bill_history_service import BillHistoryService
from backend.apps.services.income.income_history_service import \
    IncomeHistoryService


class UserService:
    @inject
    def __init__(self,
                 user_repository: UserRepository,
                 income_history_service: IncomeHistoryService,
                 bill_history_service: BillHistoryService):
        self.user_repository: UserRepository = user_repository
        self.income_history_service: IncomeHistoryService = income_history_service
        self.bill_history_service: BillHistoryService = bill_history_service

    def user_from_request(self, user_request: SignupRequest | LoginRequest) -> User:
        user: User = User(
            username=user_request.username,
            password=SafePassword(unhashed_password=user_request.password)
        )
        if isinstance(user_request, SignupRequest):
            user.email = user_request.email
        return user

    async def get_by_username(self, username: str) -> User:
        return await database_sync_to_async(self.user_repository.get_by_username)(username)

    async def get_by_id(self, user_id: int):
        # user: User = await database_sync_to_async(self.user_repository.get_by_id)(user_id)
        # bill_history = await self.get_user_bill_history(user)
        # income_history = await self.get_user_income_history(user)
        #
        # user.user_bill_history = bill_history
        # user.user_income_history = income_history
        user: User = await database_sync_to_async(self.user_repository.get_by_id)(user_id)
        bill_history: BillHistory = await self.bill_history_service.initialize_bill_history(user)
        income_history: IncomeHistory = await self.income_history_service.initialize_income_history(user)
        user.user_bill_history = bill_history
        user.user_income_history = income_history
        return user

    async def get_user_income_history(self, user: User):
        income_history_orm: IncomeHistoryOrmModel = await database_sync_to_async(
            lambda: IncomeHistoryOrmModel.objects.filter(
                id=user.user_income_history.id).first()
        )()
        one_time_incomes: list[
            OneTimeIncomeOrmModel] = await database_sync_to_async(
            lambda: list(OneTimeIncomeOrmModel.objects.filter(
                income_history=income_history_orm))
        )()
        recurring_incomes: list[
            RecurringIncomeOrmModel] = await database_sync_to_async(
            lambda: list(RecurringIncomeOrmModel.objects.filter(
                income_history=income_history_orm))
        )()
        wage_incomes: list[WageIncomeOrmModel] = await database_sync_to_async(
            lambda: list(WageIncomeOrmModel.objects.filter(
                income_history=income_history_orm))
        )()
        income_history: IncomeHistory = IncomeHistory.from_orm_model(
            income_history_orm)
        for income in one_time_incomes:
            income_history.add_one_time_income(
                await database_sync_to_async(OneTimeIncome.from_orm_model)(
                    income))
        for income in recurring_incomes:
            income_history.add_recurring_income(
                await database_sync_to_async(RecurringIncome.from_orm_model)(
                    income))
        for income in wage_incomes:
            income_history.add_wage_income(
                await database_sync_to_async(WageIncome.from_orm_model)(
                    income))
        return income_history

    async def get_user_bill_history(self, user: User):
        bill_history_orm: BillHistoryOrmModel = await database_sync_to_async(
            lambda: BillHistoryOrmModel.objects.filter(
                id=user.user_bill_history.id).first()
        )()
        one_time_bills: list[
            OneTimeBillOrmModel] = await database_sync_to_async(
            lambda: list(OneTimeBillOrmModel.objects.filter(
                bill_history=bill_history_orm))
        )()
        recurring_bills: list[
            RecurringBillOrmModel] = await database_sync_to_async(
            lambda: list(RecurringBillOrmModel.objects.filter(
                bill_history=bill_history_orm))
        )()
        bill_history = BillHistory.from_orm_model(bill_history_orm)
        for bill in one_time_bills:
            bill_history.add_one_time_bill(
                await database_sync_to_async(OneTimeBill.from_orm_model)(
                    bill))
        for bill in recurring_bills:
            bill_history.add_recurring_bill(
                await database_sync_to_async(OneTimeBill.from_orm_model)(
                    bill))
        return bill_history