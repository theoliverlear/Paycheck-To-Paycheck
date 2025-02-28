from django.db import models
from django.utils.timezone import now



class DateRangeOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    starting_date = models.DateField(default=now)
    ending_date = models.DateField(default=now)
    class Meta:
        db_table = 'date_ranges'

class DueDateOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    due_date = models.DateField(default=now)
    class Meta:
        db_table = 'due_dates'


class RecurringDateOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.DateField(default=now)
    interval = models.IntegerField(default=1)
    class Meta:
        db_table = 'recurring_dates'