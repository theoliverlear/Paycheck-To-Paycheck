from attr import attr
from attrs import define


@define
class DueDay:
    day_of_month: int = attr(default=1)