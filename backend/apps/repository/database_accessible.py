from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from backend.apps.entity.identifiable import Identifiable

T = TypeVar("T")

class DatabaseAccessible(Generic[T], ABC):
    @abstractmethod
    def save(self, model_to_save) -> T:
        pass

    @abstractmethod
    def update(self, model_to_update) -> None:
        pass

    @abstractmethod
    def get_by_id(self, identifiable: Identifiable | int) -> T:
        pass

    @abstractmethod
    def exists_by_id(self, identifiable: Identifiable | int) -> T:
        pass