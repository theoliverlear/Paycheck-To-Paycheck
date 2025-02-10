from typing import TypeVar, Generic
from rest_framework import status

from attr import attr
from attrs import define, field

T = TypeVar("T")

@define(init=False)
class PayloadStatusResponse(Generic[T]):
    payload: T = attr(default=None)
    status_code: int = field(default=status.HTTP_200_OK)
    def __init__(self,
                 payload: T,
                 status_code: int = status.HTTP_200_OK):
        super().__init__()
        self.payload = payload
        self.status_code = status_code