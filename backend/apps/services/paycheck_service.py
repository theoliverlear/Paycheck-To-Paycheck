from datetime import date

from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.time.date_range import DateRange
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.user.user import User
from backend.apps.models.date_utilities import get_bi_weeks_after_date
from backend.apps.entity.time.year_interval import YearInterval


class PaycheckService:
    def get_current_user_paycheck(self, user: User):
        paycheck: Paycheck = self.get_paycheck_from_now(user, 0)
        return paycheck

    def get_paycheck_from_now(self, user: User, num_paychecks: int):
        start_date: date = get_bi_weeks_after_date(date.today(), num_paychecks)
        user_payday: date = user.payday.day
        user_payday_end_date = get_bi_weeks_after_date(user_payday, 1)
        date_range: DateRange = DateRange(start_date=user_payday, end_date=user_payday_end_date)
        recurring_date: RecurringDate = RecurringDate(day=start_date, interval=YearInterval.BI_WEEKLY)
        while not date_range.in_range(start_date):
            next_payday: date = recurring_date.get_next_date()
            date_range = DateRange.get_paycheck_range(next_payday)
        paycheck: Paycheck = Paycheck.from_user(user, start_date=date_range.start_date)
        return paycheck

