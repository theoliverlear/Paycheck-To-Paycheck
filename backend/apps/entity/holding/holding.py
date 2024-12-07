from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable

@define
class Holding(ABC, Identifiable):
    amount: float = attr(default=0.0)