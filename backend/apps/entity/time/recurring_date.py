from attr import attr
from attrs import define

from backend.apps.entity.time.date_interval import DateInterval


@define
class RecurringDate:
    day: int = attr(default=1)
    interval: DateInterval = attr(default=DateInterval.MONTHLY)