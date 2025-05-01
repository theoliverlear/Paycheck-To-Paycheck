from rest_framework import serializers

from backend.apps.comm.serialize.entity.bill.one_time_bill_serializer import \
    OneTimeBillSerializer
from backend.apps.comm.serialize.entity.bill.recurring_bill_serializer import \
    RecurringBillSerializer
from backend.apps.comm.serialize.entity.income.one_time_income_serializer import \
    OneTimeIncomeSerializer
from backend.apps.comm.serialize.entity.income.recurring_income_serializer import \
    RecurringIncomeSerializer
from backend.apps.comm.serialize.entity.income.wage_income_serializer import \
    WageIncomeSerializer
from backend.apps.comm.serialize.entity.time.date_range_serializer import \
    DateRangeSerializer
from backend.apps.entity.paycheck.paycheck import Paycheck


class PaycheckSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    date_range = DateRangeSerializer()
    one_time_incomes = serializers.SerializerMethodField()
    recurring_incomes = serializers.SerializerMethodField()
    wage_incomes = serializers.SerializerMethodField()
    one_time_bills = serializers.SerializerMethodField()
    recurring_bills = serializers.SerializerMethodField()
    total_income = serializers.FloatField()
    total_bills = serializers.FloatField()
    left_over_income = serializers.FloatField()

    class Meta:
        model = Paycheck
        fields = '__all__'

    def get_one_time_bills(self, paycheck: Paycheck):
        return OneTimeBillSerializer(paycheck.one_time_bills, many=True).data

    def get_recurring_bills(self, paycheck: Paycheck):
        return RecurringBillSerializer(paycheck.recurring_bills, many=True).data

    def get_one_time_incomes(self, paycheck: Paycheck):
        return OneTimeIncomeSerializer(paycheck.one_time_incomes, many=True).data

    def get_recurring_incomes(self, paycheck: Paycheck):
        return RecurringIncomeSerializer(paycheck.recurring_incomes, many=True).data

    def get_wage_incomes(self, paycheck: Paycheck):
        return WageIncomeSerializer(paycheck.wage_incomes, many=True).data
