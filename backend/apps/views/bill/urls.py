from django.urls import path

from backend.apps.views.bill.get_all_bills_view import GetAllBillsView

urlpatterns = [
    path('get/all', GetAllBillsView.as_view(), name="get_all_bills"),
]