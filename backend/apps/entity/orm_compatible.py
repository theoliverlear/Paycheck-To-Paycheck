from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from attrs import define
# M = Model, O = ORM Model
M = TypeVar("M")
O = TypeVar("O")

@define
class OrmCompatible(ABC, Generic[M, O]):
    @abstractmethod
    def save(self) -> M:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def set_from_orm_model(self, orm_model) -> None:
        pass

    @abstractmethod
    def get_orm_model(self) -> O:
        pass

    @staticmethod
    @abstractmethod
    def set_orm_model(db_model, model_to_set) -> None:
        pass

    @staticmethod
    @abstractmethod
    def from_orm_model(orm_model) -> M:
        pass