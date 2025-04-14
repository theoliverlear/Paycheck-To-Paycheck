from rest_framework import serializers

from backend.apps.comm.serialize.entity.holding.saving.saving_serializer import \
    SavingSerializer
from backend.apps.entity.wallet.wallet import Wallet


class WalletSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    checking_account = SavingSerializer()

    def get_instance(self):
        return self.Meta.model(**self.validated_data)

    class Meta:
        model = Wallet
        fields = '__all__'