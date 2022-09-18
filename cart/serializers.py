from rest_framework import serializers
from cart.models import Carts, Item


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


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            "id",
            "cart",
            "product",
            "price",
            "count",
        ]
        read_only_fields = [
            "price",
        ]
