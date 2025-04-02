from attr import attr
from attrs import define

from backend.apps.entity.holding.holding import Holding
from backend.apps.entity.identifiable import Identifiable


@define
class Debt(Holding, Identifiable):
    pass