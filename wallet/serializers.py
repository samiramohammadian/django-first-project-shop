from rest_framework import serializers
from wallet.models import Charge, Cost


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = [
            "id",
            "cart",
            "amount",
            "tracking_code",
        ]

        read_only_fields = [
            "tracking_code",
        ]


class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = [
            "id",
            "user",
            "amount",
            "tracking_code",
        ]

        read_only_fields = [
            "tracking_code",
        ]