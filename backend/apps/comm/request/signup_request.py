from django.db import models

from backend.apps.comm.request.login_request import LoginRequest


class SignupRequest(models.Model, LoginRequest):
    email = models.EmailField()