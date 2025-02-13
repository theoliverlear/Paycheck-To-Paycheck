from django.db import models

from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.time.recurring_date import RecurringDateOrmModel


class IncomeTypeOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    interval = models.IntegerField(default=YearInterval.YEARLY.value)
    class Meta:
        db_table = 'income_types'

class RecurringIncomeOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    income = models.FloatField(default=0.0)
    income_type = models.ForeignKey(IncomeTypeOrmModel, on_delete=models.CASCADE)
    recurring_date = models.ForeignKey(RecurringDateOrmModel, on_delete=models.CASCADE)
    class Meta:
        db_table = 'recurring_incomes'

class IncomeOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    income = models.FloatField(default=0.0)
    income_type = models.ForeignKey(IncomeTypeOrmModel, on_delete=models.CASCADE)
    class Meta:
        db_table = 'incomes'
