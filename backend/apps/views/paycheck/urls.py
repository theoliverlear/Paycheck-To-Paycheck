from django.urls import path

from backend.apps.views.paycheck.paycheck_view import PaycheckView

urlpatterns = [
    path("get/<int:paycheck_num>",PaycheckView.as_view(), name="paycheck"),
]