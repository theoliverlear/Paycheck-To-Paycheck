from rest_framework import serializers

from backend.apps.comm.response.bills_response import BillsResponse
from backend.apps.comm.serialize.entity.bill.one_time_bill_serializer import \
    OneTimeBillSerializer
from backend.apps.comm.serialize.entity.bill.recurring_bill_serializer import \
    RecurringBillSerializer


class BillsResponseSerializer(serializers.Serializer):
    one_time_bills = serializers.SerializerMethodField()
    recurring_bills = serializers.SerializerMethodField()

    class Meta:
        model = BillsResponse
        fields = '__all__'

    def get_one_time_bills(self, bills_response: BillsResponse):
        return OneTimeBillSerializer(bills_response.one_time_bills, many=True).data

    def get_recurring_bills(self, bills_response: BillsResponse):
        return RecurringBillSerializer(bills_response.recurring_bills, many=True).data