import logging
from datetime import date

from django.http import HttpResponse
from rest_framework.views import APIView

from backend.apps.entity.income.income_types import IncomeTypes
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.paycheck.taxed_paycheck import TaxedPaycheck
from backend.apps.entity.tax.tax import Tax
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.entity.user.user import User


class PaycheckView(APIView):
    def get(self, request, params, *args, **kwargs):
        user: User = User(
            first_name='John',
            last_name='Doe',
            username='johndoe',
            password=SafePassword(unhashed_password='password'),
            recurring_income=RecurringIncome(
                income_amount=params,
                recurring_date=RecurringDate(day=date.today(), interval=YearInterval.YEARLY)
            ),
        )
        tax: Tax = Tax(25)
        taxed_paycheck: TaxedPaycheck = TaxedPaycheck(income=user.recurring_income, tax=tax)
        logging.info(taxed_paycheck)
        paycheck_str: str = f"${taxed_paycheck.total_income:,.2f}"

        paycheck_after_taxes_str: str = f"${taxed_paycheck.after_tax_income:,.2f}"
        logging.info(f"Paycheck: {paycheck_str}, After Taxes: {paycheck_after_taxes_str}")
        combined_info: str = f"Paycheck: {paycheck_str}, After Taxes: {paycheck_after_taxes_str}"
        user.save()
        return HttpResponse(combined_info)
