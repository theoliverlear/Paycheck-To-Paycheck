from rest_framework import serializers

from backend.apps.comm.response.operation_success_response import \
    OperationSuccessResponse


class OperationSuccessResponseSerializer(serializers.Serializer):
    operation_successful = serializers.BooleanField()
    class Meta:
        model = OperationSuccessResponse
        fields = '__all__'