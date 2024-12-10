from rest_framework import serializers

from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.comm.serialize.comm.request.login_request_serializer import \
    LoginRequestSerializer


class SignupRequestSerializer(serializers.Serializer, LoginRequestSerializer):
    class Meta:
        model = SignupRequest
        fields = '__all__'

    def get_instance(self):
        return self.Meta.model(**self.validated_data)