from django.urls import path
from .views import *

urlpatterns = [
    path('api/product-list/', ProductListApiView.as_view(), name='api-product-list'),
]