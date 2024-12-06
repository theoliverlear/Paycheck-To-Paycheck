from enum import Enum


class DateInterval(Enum):
    YEARLY: int = 1
    QUARTERLY: int = 4
    BI_MONTHLY: int = 6
    MONTHLY: int = 12
    BI_WEEKLY: int = 26
    WEEKLY: int = 52
    DAILY: int = 365
    HOURLY: int = 8760
    NO_INTERVAL: int = 0
    @staticmethod
    def from_interval(interval: int) -> 'DateInterval':
        for date_interval in DateInterval:
            if date_interval.value == interval:
                return date_interval
        return DateInterval.NO_INTERVAL