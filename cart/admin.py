from django.contrib import admin
from cart.models import Carts

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
