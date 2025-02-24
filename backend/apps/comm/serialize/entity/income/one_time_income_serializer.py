from rest_framework import serializers

from backend.apps.entity.income.one_time_income import OneTimeIncome


class IncomeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    income_amount = serializers.FloatField()
    class Meta:
        model = OneTimeIncome,
        fields = '__all__'