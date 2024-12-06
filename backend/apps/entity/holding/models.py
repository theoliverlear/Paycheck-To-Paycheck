from django.db import models


class HoldingOrmModel(models.Model):
    amount = models.FloatField(default=0.0)


class InterestHoldingOrmModel(models.Model):
    amount = models.FloatField(default=0.0)
    interest_rate = models.FloatField(default=0.0)
