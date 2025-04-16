from rest_framework import serializers

from backend.apps.entity.time.date_range import DateRange


class DateRangeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    class Meta:
        model = DateRange
        fields = '__all__'