from rest_framework import serializers

from backend.apps.entity.holding.saving.saving import Saving


class SavingSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=200)
    amount = serializers.FloatField()
    class Meta:
        model = Saving
        fields = '__all__'