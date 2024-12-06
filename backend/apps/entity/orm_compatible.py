from abc import ABC, abstractmethod

from attrs import define


@define
class OrmCompatible(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def set_from_orm_model(self, orm_model):
        pass

    @abstractmethod
    def get_orm_model(self):
        pass