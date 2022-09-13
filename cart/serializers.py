from rest_framework import serializers
from cart.models import Carts


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carts
        fields = [
            "id",
            "user",
            "purchase_created",
            "purchase_modified",
        ]
        read_only_fields = [
            'user',
        ]
