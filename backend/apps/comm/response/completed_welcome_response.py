from attr import attr
from attrs import define


@define
class CompletedWelcomeResponse:
    has_completed_welcome: bool = attr(default=False)