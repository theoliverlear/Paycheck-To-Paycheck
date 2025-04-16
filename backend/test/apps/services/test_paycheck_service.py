import logging
import unittest

from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.user.user import User
from backend.apps.services.paycheck_service import PaycheckService
from backend.test.setup.setup import setup_user
from backend.test.test_logging import log_test_class, log_test_results


@log_test_class(class_tested="PaycheckService")
class TestPaycheckService(unittest.TestCase):

    def setUp(self):
        self.paycheck_service = PaycheckService()

    @log_test_results
    def test_get_current_user_paycheck_exists(self):
        user: User = setup_user()
        paycheck: Paycheck = self.paycheck_service.get_current_user_paycheck(user)
        logging.info(f'Paycheck: {paycheck}')
        self.assertIsNotNone(paycheck)

    @log_test_results
    def test_get_paycheck_from_now_exists(self):
        user: User = setup_user()
        future_paycheck: Paycheck = self.paycheck_service.get_paycheck_from_now(user, 1)
        logging.info(f"Future paycheck: {future_paycheck}")
        self.assertIsNotNone(future_paycheck)

    @log_test_results
    def test_future_paycheck_is_different(self):
        user: User = setup_user()
        current_paycheck: Paycheck = self.paycheck_service.get_current_user_paycheck(user)
        future_paycheck: Paycheck = self.paycheck_service.get_paycheck_from_now(user, 2)
        logging.info(f"Current paycheck: {current_paycheck}")
        logging.info(f"Future paycheck: {future_paycheck}")
        self.assertNotEqual(current_paycheck, future_paycheck)


if __name__ == '__main__':
    unittest.main()
