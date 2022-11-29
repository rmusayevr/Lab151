from django.urls import path
from products.views import *

urlpatterns = [
    path('product-list/', ProductList.as_view(), name='product-list'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api/product-list/', ProductListApiView.as_view(), name='api-product-list'),
]