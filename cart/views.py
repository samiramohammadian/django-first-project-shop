import datetime
import http.client

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from cart.models import Carts, Item
from cart.serializers import CartSerializer, ItemSerializer


class CartView(ModelViewSet):
    queryset = Carts.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_carts = Carts.objects.filter(user=self.request.user)
        if self.request.method == "GET":
            return user_carts
        else:
            return user_carts.filter(purchase_date=None)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=["POST"], detail=True)
    def pay(self, request, pk):
        cart = self.get_object()
        cart.purchase_date = datetime.datetime.now()
        cart.save()
        ser_data = CartSerializer(cart).data
        return Response(ser_data)


class ItemView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(cart__user=self.request.user)

    @action(methods=["POST"], detail=True)
    def increase_count(self, request, pk):
        item = self.get_object()
        item.count += 1
        item.save()
        ser_item = ItemSerializer(item).data
        return Response(ser_item)

    @action(methods=["POST"], detail=True)
    def decrease_count(self, request, pk):
        item = self.get_object()
        item.count -= 1
        item.save()
        ser_item = ItemSerializer(item).data
        return Response(ser_item)
