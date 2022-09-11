from django.urls import path
from products.views import ProductView, CategoryView, CategoryViewAdmin, AdminProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', ProductView)
router.register('categories', CategoryView)
router.register('admin/categories', CategoryViewAdmin)
router.register('admin/products', AdminProductView)
urlpatterns = [

]+router.urls
