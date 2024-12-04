from django.http import HttpResponse
from rest_framework.views import APIView

from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.user.user import User


class PaycheckView(APIView):
    def get(self, request, params, *args, **kwargs):
        user = User(income=params)
        paycheck = Paycheck(user.income)
        return HttpResponse(paycheck)