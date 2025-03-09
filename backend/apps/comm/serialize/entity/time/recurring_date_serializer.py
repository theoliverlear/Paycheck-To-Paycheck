from rest_framework import serializers

from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval


class RecurringDateSerializer(serializers.Serializer):
    day = serializers.DateField()
    interval = serializers.SerializerMethodField()
    class Meta:
        model = RecurringDate
        fields = '__all__'

    def get_interval(self, object):
        if isinstance(object.interval, YearInterval):
            return object.interval.value
        return object.interval
