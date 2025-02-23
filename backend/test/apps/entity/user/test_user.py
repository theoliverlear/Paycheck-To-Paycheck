import unittest
from datetime import date

import django

from backend.apps.entity.income.income_types import IncomeTypes
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.entity.user.user import User

django.setup()

recurring_date: RecurringDate = RecurringDate(day=date.today(),
                                              interval=YearInterval.YEARLY)
recurring_income: RecurringIncome = RecurringIncome(name="Walmart Income",
                                                    income_amount=43_000,
                                                    recurring_date=recurring_date)
safe_password: SafePassword = SafePassword(unhashed_password='password')

def setup_user() -> User:
    user: User = User(
        first_name='John',
        last_name='Doe',
        username='johndoe',
        recurring_income=recurring_income,
        password=safe_password
    )
    return user

class MyTestCase(unittest.TestCase):
    def test_user_exists(self):
        user: User = setup_user()
        self.assertIsNotNone(user)

    def test_orm_model_exists(self):
        user: User = setup_user()
        self.assertIsNotNone(user.get_orm_model())

    def test_save(self):
        try:
            user: User = setup_user()
            saved_user: User = user.save()
            self.assertIsNotNone(saved_user)
        except Exception as exception:
            self.fail(exception)

    def test_update(self):
        try:
            user: User = setup_user()
            user.first_name = 'Jack'
            saved_user: User = user.save()
            saved_user.first_name = 'Jane'
            saved_user.update()
        except Exception as exception:
            self.fail(exception)
if __name__ == '__main__':
    unittest.main()
