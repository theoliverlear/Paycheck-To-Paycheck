from rest_framework import serializers

from backend.apps.comm.request.login_request import LoginRequest


class LoginRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginRequest
        fields = '__all__'

    def get_instance(self):
        return self.Meta.model(**self.validated_data)