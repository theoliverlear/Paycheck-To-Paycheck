from attr import attr
from attrs import define


@define
class AuthStatus:
    is_authorized: bool = attr(default=False)