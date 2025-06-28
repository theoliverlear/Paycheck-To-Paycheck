from rest_framework import serializers

from backend.apps.comm.response.completed_welcome_response import \
    CompletedWelcomeResponse


class CompletedWelcomeResponseSerializer(serializers.Serializer):
    has_completed_welcome = serializers.BooleanField()
    class Meta:
        fields = '__all__'
        model = CompletedWelcomeResponse