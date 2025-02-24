from django.db import models

from backend.apps.entity.income.models import RecurringIncomeOrmModel
from backend.apps.entity.tax.models import TaxOrmModel


class PaycheckOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    income = models.OneToOneField(RecurringIncomeOrmModel, on_delete=models.CASCADE)
    paycheck_income = models.FloatField(default=0.0)
    class Meta:
        db_table = 'paychecks'

class TaxedPaycheckOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    income = models.OneToOneField(RecurringIncomeOrmModel, on_delete=models.CASCADE)
    paycheck_income = models.FloatField(default=0.0)
    tax = models.ForeignKey(TaxOrmModel, on_delete=models.CASCADE)
    after_tax_income = models.FloatField(default=0.0)
    deducted_from_paycheck = models.FloatField(default=0.0)
    class Meta:
        db_table = 'taxed_paychecks'