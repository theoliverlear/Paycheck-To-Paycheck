from django.db import models


class TaxOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    rate = models.FloatField(default=0.0)
    class Meta:
        db_table = 'taxes'

class TaxWithholdingOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    total_withheld = models.FloatField(default=0.0)
    class Meta:
        db_table = 'tax_withholdings'