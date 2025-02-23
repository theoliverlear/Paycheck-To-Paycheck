from enum import Enum

from backend.apps.entity.income.income_type import IncomeType
from backend.apps.entity.time.year_interval import YearInterval


class IncomeTypes(Enum):
    SALARY       = IncomeType(interval=YearInterval.YEARLY)
    PAYCHECK     = IncomeType(interval=YearInterval.BI_WEEKLY)
    WAGE         = IncomeType(interval=YearInterval.HOURLY)
    MONTHLY      = IncomeType(interval=YearInterval.MONTHLY)
    ONE_TIME     = IncomeType(interval=YearInterval.NO_INTERVAL)
    YEARLY_BONUS = IncomeType(interval=YearInterval.YEARLY)
    TAX_REFUND   = IncomeType(interval=YearInterval.YEARLY)