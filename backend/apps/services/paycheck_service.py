from datetime import date

from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.time.date_range import DateRange
from backend.apps.entity.user.user import User
from backend.apps.models.date_utilities import get_bi_weeks_after_date, \
    get_num_bi_weeks_between_dates


class PaycheckService:
    def get_current_user_paycheck(self, user: User):
        paycheck: Paycheck = self.get_paycheck_from_now(user, 0)
        return paycheck

    def get_paycheck_from_now(self, user: User, num_paychecks: int):
        user_payday: date = user.payday.day
        initial_payday_bi_weeks_gap: int  = get_num_bi_weeks_between_dates(user_payday, date.today())
        total_paychecks: int = initial_payday_bi_weeks_gap + num_paychecks
        start_date: date = get_bi_weeks_after_date(user_payday, total_paychecks)
        user_payday_end_date = get_bi_weeks_after_date(start_date, 1)
        date_range: DateRange = DateRange(start_date=start_date, end_date=user_payday_end_date)
        paycheck: Paycheck = Paycheck.from_user(user, start_date=date_range.start_date)
        return paycheck

    def get_all_paychecks_from_now(self, user: User, num_paychecks: int) -> list[Paycheck]:
        paychecks: list[Paycheck] = []
        for i in range(num_paychecks + 1):
            paycheck: Paycheck = self.get_paycheck_from_now(user, i)
            paychecks.append(paycheck)
            print(f"Paycheck {i}: {paycheck}")
        return paychecks

    def get_wallet_from_future_paychecks(self, user: User, num_paychecks: int) -> float:
        user_wallet_amount: float = user.wallet.checking_account.amount
        print("Amount: ", user_wallet_amount)
        # paychecks: list[Paycheck] = self.get_all_paychecks_from_now(user, num_paychecks)
        # print('Num paychecks: ', len(paychecks), " num asked for: ", num_paychecks)
        # for paycheck in paychecks:
        #     print(paycheck)
        #     user_wallet_amount += paycheck.left_over_income
        #     print('Found left over income: ', paycheck.left_over_income)
        # print("Total Amount: ", user_wallet_amount)
        for i in range(num_paychecks + 1):
            paycheck: Paycheck = self.get_paycheck_from_now(user, i)
            user_wallet_amount += paycheck.left_over_income
            print(f"Paycheck {i} left over income: {paycheck.left_over_income}, Total Amount: {user_wallet_amount}")

        return user_wallet_amount

