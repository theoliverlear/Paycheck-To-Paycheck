from django.db import models

from backend.apps.entity.time.models import DueDateOrmModel
from backend.apps.entity.time.recurring_date import RecurringDateOrmModel

class OneTimeBillOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.FloatField(default=0.0)
    due_date = models.ForeignKey(DueDateOrmModel, on_delete=models.CASCADE)
    bill_history = models.ForeignKey('BillHistoryOrmModel', on_delete=models.CASCADE, default=None, null=True)
    class Meta:
        db_table = 'one_time_bills'

class RecurringBillOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.FloatField(default=0.0)
    recurring_date = models.ForeignKey(RecurringDateOrmModel, on_delete=models.CASCADE)
    bill_history = models.ForeignKey('BillHistoryOrmModel', on_delete=models.CASCADE, default=None, null=True)
    class Meta:
        db_table = 'recurring_bills'

class BillHistoryOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'bill_histories'