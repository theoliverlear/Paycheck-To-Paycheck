from attr import attr
from attrs import define

from backend.apps.entity.holding.holding import Holding

@define
class Saving(Holding):
    amount: float = attr(default=0.0)