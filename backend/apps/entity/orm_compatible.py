from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from attrs import define
# M = Model, O = ORM Model
M = TypeVar("M")
O = TypeVar("O")

@define
class OrmCompatible(ABC, Generic[M, O]):
    @abstractmethod
    def save(self: M) -> M:
        pass

    @abstractmethod
    def update(self: M) -> None:
        pass

    @abstractmethod
    def set_from_orm_model(self: M, orm_model: O) -> None:
        pass

    @abstractmethod
    def get_orm_model(self: M) -> O:
        pass

    @staticmethod
    @abstractmethod
    def set_orm_model(db_model: O, model_to_set: O) -> None:
        pass

    @staticmethod
    @abstractmethod
    def from_orm_model(orm_model: O) -> M:
        pass