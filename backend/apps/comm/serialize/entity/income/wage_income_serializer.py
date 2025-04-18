from rest_framework import serializers

from backend.apps.comm.serialize.entity.time.recurring_date_serializer import \
    RecurringDateSerializer
from backend.apps.entity.income.wage_income import WageIncome


class WageIncomeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    amount = serializers.FloatField()
    yearly_income = serializers.FloatField()
    weekly_hours = serializers.FloatField()
    recurring_date = RecurringDateSerializer()
    class Meta:
        model = WageIncome
        fields = '__all__'