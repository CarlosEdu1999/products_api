from django.contrib import admin
from django.urls import path, include
from products.views import ProductsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductsViewSet, basename='Products')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
