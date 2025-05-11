from django.urls import path

from backend.apps.views.income.delete_one_time_income_view import \
    DeleteOneTimeIncomeView
from backend.apps.views.income.delete_recurring_income_view import \
    DeleteRecurringIncomeView
from backend.apps.views.income.delete_wage_income_view import \
    DeleteWageIncomeView
from backend.apps.views.income.get_all_incomes_view import GetAllIncomesView

urlpatterns = [
    path('get/all', GetAllIncomesView.as_view(), name="get_all_incomes"),
    path('delete/one-time/<int:income_id>', DeleteOneTimeIncomeView.as_view(), name="delete_one_time_income"),
    path('delete/recurring/<int:income_id>', DeleteRecurringIncomeView.as_view(), name="delete_recurring_income"),
    path('delete/wage/<int:income_id>', DeleteWageIncomeView.as_view(), name="delete_wage_income"),
]