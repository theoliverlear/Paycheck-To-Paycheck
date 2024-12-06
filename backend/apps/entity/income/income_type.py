from attr import attr
from attrs import define

from backend.apps.entity.time.date_interval import DateInterval

@define
class IncomeType:
    name: str = attr(default="")
    interval: DateInterval = attr(default=DateInterval.MONTHLY)