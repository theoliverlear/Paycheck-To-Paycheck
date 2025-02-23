from rest_framework import serializers

from backend.apps.entity.income.income_type import IncomeType


class IncomeTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    interval = serializers.IntegerField()
    class Meta:
        model = IncomeType,
        fields = '__all__'