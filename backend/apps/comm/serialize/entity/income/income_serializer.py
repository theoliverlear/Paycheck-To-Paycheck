from rest_framework import serializers

from backend.apps.entity.income.income import Income


class IncomeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    income_amount = serializers.FloatField()
    class Meta:
        model = Income,
        fields = '__all__'