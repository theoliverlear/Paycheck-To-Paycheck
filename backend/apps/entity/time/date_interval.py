from enum import Enum


class DateInterval(Enum):
    YEARLY = 1,
    QUARTERLY = 4,
    BI_MONTHLY = 6,
    MONTHLY = 12,
    BI_WEEKLY = 26,
    WEEKLY = 52
    DAILY = 365,
    HOURLY = 8760,
    NO_INTERVAL = 0