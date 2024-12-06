from django.db import models


class InterestSavingOrmModel(models.Model):
    amount = models.FloatField(default=0.0)
    interest_rate = models.FloatField(default=0.0)
    class Meta:
        db_table = 'interest_savings'

class SavingOrmModel(models.Model):
    amount = models.FloatField(default=0.0)
    class Meta:
        db_table = 'savings'