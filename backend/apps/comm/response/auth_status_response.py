from attr import attr
from attrs import define

from backend.apps.models.http.auth_status import AuthStatus


@define(init=False)
class AuthStatusResponse:
    is_authorized: bool = attr(default=False)
    def __init__(self,
                 auth_status: AuthStatus = AuthStatus.UNAUTHORIZED):
        self.is_authorized = auth_status.value