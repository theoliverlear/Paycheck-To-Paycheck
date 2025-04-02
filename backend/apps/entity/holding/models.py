from django.db import models


class HoldingOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="")
    amount = models.FloatField(default=0.0)
    class Meta:
        db_table = 'holdings'


class InterestHoldingOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="")
    amount = models.FloatField(default=0.0)
    interest_rate = models.FloatField(default=0.0)
    class Meta:
        db_table = 'interest_holdings'
