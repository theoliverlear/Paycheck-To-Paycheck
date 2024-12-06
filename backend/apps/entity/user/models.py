from django.db import models

from backend.apps.entity.income.models import RecurringIncomeOrmModel


class SafePasswordOrmModel(models.Model):
    encoded_password = models.CharField(max_length=100)
    class Meta:
        db_table = 'passwords'

class UserOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    username = models.CharField(max_length=100, default="")
    recurring_income = models.ForeignKey(RecurringIncomeOrmModel, on_delete=models.CASCADE)
    password = models.ForeignKey(SafePasswordOrmModel, on_delete=models.CASCADE)
    class Meta:
        db_table = 'users'