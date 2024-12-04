from attr import attr
from attrs import define

@define
class Income:
    income: float = attr(default=0.0)