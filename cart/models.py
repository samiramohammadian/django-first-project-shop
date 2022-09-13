from django.db import models
from users.models import User
# Create your models here.


class Carts(models.Model):

    #purchase_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_created = models.DateTimeField(auto_now_add=True)
    purchase_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id}, {self.purchase_modified}, {self.purchase_created}"
