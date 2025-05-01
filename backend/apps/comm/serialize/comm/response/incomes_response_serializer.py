from rest_framework import serializers

from backend.apps.comm.response.income_response import IncomesResponse
from backend.apps.comm.serialize.entity.income.one_time_income_serializer import \
    OneTimeIncomeSerializer
from backend.apps.comm.serialize.entity.income.recurring_income_serializer import \
    RecurringIncomeSerializer
from backend.apps.comm.serialize.entity.income.wage_income_serializer import \
    WageIncomeSerializer


class IncomesResponseSerializer(serializers.Serializer):
    one_time_incomes = serializers.SerializerMethodField()
    recurring_incomes = serializers.SerializerMethodField()
    wage_incomes = serializers.SerializerMethodField()

    class Meta:
        model = IncomesResponse
        fields = '__all__'

    def get_one_time_incomes(self, obj: IncomesResponse):
        return OneTimeIncomeSerializer(obj.one_time_incomes, many=True).data

    def get_recurring_incomes(self, obj: IncomesResponse):
        return RecurringIncomeSerializer(obj.recurring_incomes, many=True).data

    def get_wage_incomes(self, obj: IncomesResponse):
        return WageIncomeSerializer(obj.wage_incomes, many=True).data