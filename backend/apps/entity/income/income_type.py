from enum import Enum

from backend.apps.entity.time.date_interval import DateInterval

class IncomeType(Enum):
    SALARY = ('salary', DateInterval.YEARLY),
    PAYCHECK = ('paycheck', DateInterval.BI_WEEKLY),
    WAGE = ('wage', DateInterval.HOURLY),
    ONE_TIME = ('one_time', DateInterval.NO_INTERVAL),
    YEARLY_BONUS = ('yearly_bonus', DateInterval.YEARLY),
    TAX_REFUND = ('tax_refund', DateInterval.YEARLY),