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

