from rest_framework import serializers

from backend.apps.entity.time.due_date import DueDate


class DueDateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    due_date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = DueDate,
        fields = '__all__'