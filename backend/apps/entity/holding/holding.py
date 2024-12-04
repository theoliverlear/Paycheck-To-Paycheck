from abc import ABC

from attr import attr
from attrs import define


@define
class Holding(ABC):
    amount: float = attr(default=0.0)