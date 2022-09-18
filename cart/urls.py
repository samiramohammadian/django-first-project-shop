from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cart.views import CartView, ItemView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('carts', CartView)
router.register('items', ItemView)
urlpatterns = [

]+router.urls

