from rest_framework import serializers

from backend.apps.comm.serialize.entity.time.recurring_date_serializer import \
    RecurringDateSerializer
from backend.apps.entity.bill.recurring_bill import RecurringBill


class RecurringBillSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    amount = serializers.FloatField()
    recurring_date = RecurringDateSerializer()
    class Meta:
        model = RecurringBill
        fields = '__all__'