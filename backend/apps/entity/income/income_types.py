from enum import Enum

from backend.apps.entity.income.income_type import IncomeType
from backend.apps.entity.time.year_interval import YearInterval


class IncomeTypes(Enum):
    SALARY       = IncomeType(name='salary',
                              interval=YearInterval.YEARLY)
    PAYCHECK     = IncomeType(name='paycheck',
                              interval=YearInterval.BI_WEEKLY)
    WAGE         = IncomeType(name='wage',
                              interval=YearInterval.HOURLY)
    MONTHLY      = IncomeType(name='monthly',
                              interval=YearInterval.MONTHLY)
    ONE_TIME     = IncomeType(name='one time',
                              interval=YearInterval.NO_INTERVAL)
    YEARLY_BONUS = IncomeType(name='yearly bonus',
                              interval=YearInterval.YEARLY)
    TAX_REFUND   = IncomeType(name='tax refund',
                              interval=YearInterval.YEARLY)