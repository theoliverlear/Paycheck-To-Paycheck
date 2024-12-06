import unittest

import django

from backend.apps.entity.income.income import Income
from backend.apps.entity.income.income_type import IncomeType
from backend.apps.entity.income.income_types import IncomeTypes
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.time.date_interval import DateInterval
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.entity.user.user import User

django.setup()

recurring_date: RecurringDate = RecurringDate(1,
                                              DateInterval.YEARLY)
recurring_income: RecurringIncome = RecurringIncome(income=43_000,
                                                    income_type=IncomeTypes.SALARY.value,
                                                    recurring_date=recurring_date)
safe_password: SafePassword = SafePassword('password')

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
            user.recurring_income.recurring_date.save()
            user.recurring_income.save()
            user.password.save()
            user.save()
        except Exception as exception:
            self.fail(exception)
if __name__ == '__main__':
    unittest.main()
