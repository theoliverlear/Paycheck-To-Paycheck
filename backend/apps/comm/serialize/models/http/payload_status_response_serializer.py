from rest_framework import serializers

from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.comm.response.operation_success_response import \
    OperationSuccessResponse
from backend.apps.comm.serialize.comm.response.auth_status_response_serializer import \
    AuthStatusResponseSerializer
from backend.apps.comm.serialize.comm.response.operation_success_response_serializer import \
    OperationSuccessResponseSerializer
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse


class PayloadStatusResponseSerializer(serializers.Serializer):
    payload = serializers.SerializerMethodField()
    status_code = serializers.IntegerField

    class Meta:
        model = PayloadStatusResponse
        fields = '__all__'

    def get_payload(self, object):
        if isinstance(object.payload, AuthStatusResponse):
            serializer: AuthStatusResponseSerializer = AuthStatusResponseSerializer(object.payload)
            return serializer.data
        if isinstance(object.payload, OperationSuccessResponse):
            serializer: OperationSuccessResponseSerializer = OperationSuccessResponseSerializer(object.payload)
            return serializer.data
        return object.payload
