from attr import attr
from attrs import define


@define
class OperationSuccessResponse:
    operation_success: bool = attr(default=False)