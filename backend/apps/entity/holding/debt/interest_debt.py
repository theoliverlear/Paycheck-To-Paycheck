from attr import attr
from attrs import define

from backend.apps.entity.holding.interest_holding import InterestHolding

@define
class InterestDebt(InterestHolding):
    interest_rate: float = attr(default=0.00)