from enum import Enum


class DateInterval(Enum):
    DAYS_IN_WEEK: int = 7
    DAYS_IN_BI_WEEK: int = 14
    DAYS_IN_YEAR: int = 365
    WEEKS_IN_MONTH: int = 4
    WEEKS_IN_YEAR: int = 52