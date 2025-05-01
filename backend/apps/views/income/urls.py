from django.urls import path

from backend.apps.views.income.get_all_incomes_view import GetAllIncomesView

urlpatterns = [
    path('get/all', GetAllIncomesView.as_view(), name="get_all_incomes"),
]