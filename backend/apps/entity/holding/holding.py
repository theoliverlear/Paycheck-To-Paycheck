from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.wallet.wallet import Wallet


@define
class Holding(ABC, Identifiable):
    name: str = attr(default="")
    amount: float = attr(default=0.0)
    wallet: Wallet = attr(factory=Wallet)