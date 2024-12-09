from rest_framework import serializers

from backend.apps.comm.request.user_request import UserRequest


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = '__all__'

    def get_instance(self):
        return self.Meta.model(**self.validated_data)