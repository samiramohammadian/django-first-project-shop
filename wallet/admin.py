from django.contrib import admin
from wallet.models import Charge, Cost


@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    model = Cost
    list_display = [
        "id",
        "cart",
        "amount",
        "tracking_code",
    ]


@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    model = Charge
    list_display = [
        "id",
        "user",
        "amount",
        "tracking_code",
    ]