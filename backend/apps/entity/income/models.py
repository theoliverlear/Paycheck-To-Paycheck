from django.db import models
from django.utils.timezone import now

from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.time.recurring_date import RecurringDateOrmModel


class IncomeTypeOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    interval = models.IntegerField(default=YearInterval.YEARLY.value)
    class Meta:
        db_table = 'income_types'

class OneTimeIncomeOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    amount = models.FloatField(default=0.0)
    date_received = models.DateField(default=now)
    income_history = models.ForeignKey('IncomeHistoryOrmModel',
                                       on_delete=models.CASCADE,
                                       default=None,
                                       null=False,
                                       related_name='one_time_incomes')
    class Meta:
        db_table = 'one_time_incomes'

class RecurringIncomeOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    amount = models.FloatField(default=0.0)
    recurring_date = models.ForeignKey(RecurringDateOrmModel, on_delete=models.CASCADE)
    income_history = models.ForeignKey('IncomeHistoryOrmModel',
                                       on_delete=models.CASCADE,
                                       default=None,
                                       null=False,
                                       related_name='recurring_incomes')
    class Meta:
        db_table = 'recurring_incomes'

class WageIncomeOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    amount = models.FloatField(default=0.0)
    recurring_date = models.ForeignKey(RecurringDateOrmModel, on_delete=models.CASCADE)
    weekly_hours = models.FloatField(default=0.0)
    income_history = models.ForeignKey('IncomeHistoryOrmModel',
                                        on_delete=models.CASCADE,
                                        default=None,
                                        null=False,
                                       related_name='wage_incomes')
    class Meta:
        db_table = 'wage_incomes'

class IncomeHistoryOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'income_histories'
        abstract = False