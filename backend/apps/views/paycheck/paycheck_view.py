import logging
from datetime import date

from django.http import HttpResponse
from injector import inject
from rest_framework.views import APIView

from backend.apps.services.auth_service import AuthService


class PaycheckView(APIView):
    @inject
    def __init__(self,
                 auth_service: AuthService):
        super().__init__()
        self.auth_service: AuthService = auth_service
    def get(self, request, params, *args, **kwargs):
        logging.info(params)
        pass

