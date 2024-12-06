from django.db import models

from backend.apps.entity.income.income_types import IncomeTypes
from backend.apps.entity.time.date_interval import DateInterval
from backend.apps.entity.time.recurring_date import RecurringDateOrmModel


class IncomeOrmModel(models.Model):
    income = models.FloatField(default=0.0)
    income_type = models.CharField(max_length=100, default=IncomeTypes.SALARY)
    class Meta:
        db_table = 'incomes'

class IncomeTypeOrmModel(models.Model):
    name = models.CharField(max_length=255)
    interval = models.IntegerField(default=DateInterval.YEARLY.value)
    class Meta:
        db_table = 'income_types'

class RecurringIncomeOrmModel(models.Model):
    income = models.FloatField(default=0.0)
    income_type = models.CharField(max_length=100, default=IncomeTypes.SALARY)
    recurring_date = models.ForeignKey(RecurringDateOrmModel, on_delete=models.CASCADE)
    class Meta:
        db_table = 'recurring_incomes'