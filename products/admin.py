from django.contrib import admin
from products.models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = [
        "name",
    ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = [
        "name",
        "count",
        "price",
        "category",
    ]
    list_filter = [
        "category",
    ]