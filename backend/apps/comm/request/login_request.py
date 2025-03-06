from attr import attr
from attrs import define
from django.db import models

@define
class LoginRequest:
    username: str = attr(default="")
    password: str = attr(default="")