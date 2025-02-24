from typing import TypeVar, Generic, Type

from attr import fields

T = TypeVar("T")

class ClassFieldParser(Generic[T]):
    target_class: Type[T]
    def __init__(self, target_class: Type[T]):
        self.target_class = target_class

    def get_class_fields(self) -> list[str]:
        field_names: list[str] = []
        for field in fields(self.target_class):
            if not field.name.startswith("_"):
                field_names.append(field.name)
        return field_names