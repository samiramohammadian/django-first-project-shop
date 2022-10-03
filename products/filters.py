import django_filters
from products.models import Product


class ProductPublicFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt'],
            'category': ['exact']
        }

