from enum import Enum

from backend.apps.entity.income.income_type import IncomeType
from backend.apps.entity.time.date_interval import DateInterval


class IncomeTypes(Enum):
    SALARY       = IncomeType(name='salary',
                              interval=DateInterval.YEARLY)
    PAYCHECK     = IncomeType(name='paycheck',
                              interval=DateInterval.BI_WEEKLY)
    WAGE         = IncomeType(name='wage',
                              interval=DateInterval.HOURLY)
    ONE_TIME     = IncomeType(name='one time',
                              interval=DateInterval.NO_INTERVAL)
    YEARLY_BONUS = IncomeType(name='yearly bonus',
                              interval=DateInterval.YEARLY)
    TAX_REFUND   = IncomeType(name='tax refund',
                              interval=DateInterval.YEARLY)