from django.db import models
from users.models import User
from products.models import Product
# Create your models here.


class Carts(models.Model):
    purchase_date = models.DateTimeField(null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_created = models.DateTimeField(auto_now_add=True)
    purchase_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}- {self.id}"


class Item(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cart}, {self.product}, {self.price}, {self.count}"
