from rest_framework import serializers

from backend.apps.comm.serialize.entity.time.due_date_serializer import \
    DueDateSerializer
from backend.apps.entity.bill.bill import Bill


class BillSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255)
    amount = serializers.FloatField()
    due_date = DueDateSerializer()
    class Meta:
        model = Bill
        fields = '__all__'

    def get_instance(self):
        return self.Meta.model(**self.validated_data)