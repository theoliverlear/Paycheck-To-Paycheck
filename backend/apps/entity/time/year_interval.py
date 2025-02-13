from enum import Enum


class YearInterval(Enum):
    NO_INTERVAL: int = 0
    HOURLY: int = 8760
    DAILY: int = 365
    WEEKLY: int = 52
    BI_WEEKLY: int = 26
    MONTHLY: int = 12
    BI_MONTHLY: int = 6
    QUARTERLY: int = 4
    YEARLY: int = 1
    @staticmethod
    def from_interval(interval: int) -> 'YearInterval':
        for year_interval in YearInterval:
            if year_interval.value == interval:
                return year_interval
        return YearInterval.NO_INTERVAL