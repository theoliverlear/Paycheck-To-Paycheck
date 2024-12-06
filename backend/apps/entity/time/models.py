from django.db import models
from django.utils.timezone import now



class DateRangeOrmModel(models.Model):
    starting_date = models.DateField(default=now)
    ending_date = models.DateField(default=now)
    class Meta:
        db_table = 'date_ranges'

class DueDateOrmModel(models.Model):
    due_date = models.DateField(default=now)
    class Meta:
        db_table = 'due_dates'


class RecurringDateOrmModel(models.Model):
    day = models.IntegerField(default=1)
    interval = models.IntegerField(default=1)
    class Meta:
        db_table = 'recurring_dates'