from rest_framework import serializers

from backend.apps.comm.serialize.entity.time.recurring_date_serializer import \
    RecurringDateSerializer
from backend.apps.entity.income.recurring_income import RecurringIncome


class RecurringIncomeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    amount = serializers.FloatField()
    recurring_date = RecurringDateSerializer()
    yearly_income = serializers.FloatField()
    class Meta:
        model = RecurringIncome
        fields = '__all__'