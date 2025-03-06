from attr import attr
from attrs import define
from django.db import models

from backend.apps.comm.request.login_request import LoginRequest

@define
class SignupRequest(LoginRequest):
    email: str = attr(default="")