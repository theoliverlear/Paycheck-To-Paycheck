from django.db import models

from backend.apps.entity.time.models import DueDateOrmModel
from backend.apps.entity.time.recurring_date import RecurringDateOrmModel


class BillOrmModel(models.Model):
    name = models.CharField(max_length=255)
    amount = models.FloatField(default=0.0)
    due_date = models.ForeignKey(DueDateOrmModel, on_delete=models.CASCADE)
    class Meta:
        db_table = 'bills'

class RecurringBillOrmModel(models.Model):
    name = models.CharField(max_length=255)
    amount = models.FloatField(default=0.0)
    recurring_date = models.ForeignKey(RecurringDateOrmModel, on_delete=models.CASCADE)
    class Meta:
        db_table = 'recurring_bills'