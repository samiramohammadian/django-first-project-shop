from django.contrib import admin
from cart.models import Carts, Item

# Register your models here.


@admin.register(Carts)
class CartAdmin(admin.ModelAdmin):
    model = Carts
    list_display = [
        "id",
        "user",
        "purchase_created",
        "purchase_modified",
    ]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = [
        "id",
        "cart",
        "product",
        "price",
        "count",
    ]
