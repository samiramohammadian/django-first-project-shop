from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly

from cart.models import Carts, Item
from cart.serializers import CartSerializer, ItemSerializer


class CartView(ModelViewSet):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ItemView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(cart__user=self.request.user)

