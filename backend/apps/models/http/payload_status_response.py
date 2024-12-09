from typing import TypeVar, Generic

from attr import attr
from attrs import define

T = TypeVar('T')

@define
class PayloadStatusResponse(Generic[T]):
    payload: T = attr(factory=T)
    status: int = attr(default=200)