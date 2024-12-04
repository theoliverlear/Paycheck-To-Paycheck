from attr import attr
from attrs import define

from backend.apps.entity.holding.holding import Holding


@define
class InterestHolding(Holding):
    interest_rate: float = attr(default=0.00)