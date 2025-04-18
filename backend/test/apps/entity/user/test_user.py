import asyncio
import logging
import unittest
from datetime import date

import django
from asgiref.sync import sync_to_async

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.entity.user.user import User
from backend.apps.entity.wallet.wallet import Wallet
from backend.test.test_logging import log_test_results, log_test_class
asyncio.get_event_loop().set_debug(False)
logging.getLogger('asyncio').setLevel(logging.ERROR)

django.setup()

recurring_date: RecurringDate = RecurringDate(day=date.today(),
                                              interval=YearInterval.YEARLY)
recurring_income: RecurringIncome = RecurringIncome(name="Walmart Income",
                                                    amount=43_000,
                                                    recurring_date=recurring_date)
safe_password: SafePassword = SafePassword(unhashed_password='password')

def setup_user() -> User:
    user: User = User(
        first_name='John',
        last_name='Doe',
        username='johndoe',
        password=safe_password,
        user_income_history=IncomeHistory(),
        user_bill_history=BillHistory(),
        wallet=Wallet()
    )
    return user

@log_test_class(class_tested='User')
class UserTest(unittest.IsolatedAsyncioTestCase):
    @log_test_results
    def test_user_exists(self):
        user: User = setup_user()
        self.assertIsNotNone(user)

    @log_test_results
    def test_orm_model_exists(self):
        user: User = setup_user()
        self.assertIsNotNone(user.get_orm_model())

    @log_test_results
    async def test_save(self):
        try:
            user: User = setup_user()
            saved_user: User = await user.save()
            self.assertIsNotNone(saved_user)
        except Exception as exception:
            self.fail(exception)

    @log_test_results
    async def test_update(self):
        try:
            user: User = setup_user()
            user.first_name = 'Jack'
            saved_user: User = await user.save()
            saved_user.first_name = 'Jane'
            await saved_user.update()
        except Exception as exception:
            self.fail(exception)

if __name__ == '__main__':
    unittest.main()
