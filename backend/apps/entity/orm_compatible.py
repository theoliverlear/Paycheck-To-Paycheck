from abc import ABC, abstractmethod
from typing import TypeVar

from attrs import define

T = TypeVar("T")

@define
class OrmCompatible(ABC):
    @abstractmethod
    def save(self) -> T:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def set_from_orm_model(self, orm_model) -> None:
        pass

    @abstractmethod
    def get_orm_model(self):
        pass

    @staticmethod
    @abstractmethod
    def set_orm_model(db_model, model_to_set) -> None:
        pass

    @staticmethod
    @abstractmethod
    def from_orm_model(orm_model) -> T:
        pass