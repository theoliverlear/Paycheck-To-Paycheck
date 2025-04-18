from rest_framework import serializers

from backend.apps.entity.income.one_time_income import OneTimeIncome


class OneTimeIncomeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    amount = serializers.FloatField()
    date_received = serializers.DateField()
    class Meta:
        model = OneTimeIncome,
        fields = '__all__'