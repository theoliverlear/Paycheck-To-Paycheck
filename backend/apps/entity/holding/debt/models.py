from django.db import models


class DebtOrmModel(models.Model):
    amount = models.FloatField(default=0.0)
    class Meta:
        db_table = 'debts'

class InterestDebtOrmModel(models.Model):
    amount = models.FloatField(default=0.0)
    interest_rate = models.FloatField(default=0.0)
    class Meta:
        db_table = 'interest_debts'