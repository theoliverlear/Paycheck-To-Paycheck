from django.http import HttpResponse
from rest_framework.views import APIView

from backend.apps.entity.paycheck.paycheck import Paycheck
from backend.apps.entity.user.user import User


class PaycheckView(APIView):
    def get(self, request, params, *args, **kwargs):
        user = User(recurring_income=params)
        paycheck = Paycheck(user.recurring_income)
        return HttpResponse(paycheck)