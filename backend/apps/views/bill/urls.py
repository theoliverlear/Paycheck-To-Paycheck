from django.urls import path

from backend.apps.views.bill.delete_one_time_bill_view import \
    DeleteOneTimeBillView
from backend.apps.views.bill.delete_recurring_bill_view import \
    DeleteRecurringBillView
from backend.apps.views.bill.get_all_bills_view import GetAllBillsView

urlpatterns = [
    path('get/all', GetAllBillsView.as_view(), name="get_all_bills"),
    path('delete/one-time/<int:bill_id>', DeleteOneTimeBillView.as_view(), name="delete_one_time_bill"),
    path('delete/recurring/<int:bill_id>', DeleteRecurringBillView.as_view(), name="delete_recurring_bill"),
]