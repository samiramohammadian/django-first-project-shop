import django_filters
from cart.models import Carts


class CartPublicFilter(django_filters.FilterSet):
    class Meta:
        model = Carts
        fields = {
            'purchase_date': ['isnull']
        }
