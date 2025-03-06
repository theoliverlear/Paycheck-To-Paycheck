from rest_framework import serializers

from backend.apps.comm.response.auth_status_response import AuthStatusResponse


class AuthStatusResponseSerializer(serializers.Serializer):
    is_authorized = serializers.BooleanField(default=False)
    class Meta:
        model = AuthStatusResponse
        fields = '__all__'



    def get_instance(self):
        return self.Meta.model(**self.validated_data)
