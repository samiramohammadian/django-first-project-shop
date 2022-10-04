from django.db import models
from cart.models import Carts
from users.models import User


class Cost(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    tracking_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.cart}, {self.amount}"


class Charge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    tracking_code = models.CharField(max_length=1000 , unique=True)

    def __str__(self):
        return f"{self.user}, {self.amount}"