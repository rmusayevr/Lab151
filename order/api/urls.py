from django.urls import path
from .views import *

urlpatterns = [
    path('api/basket/', BasketApiView.as_view(), name='api-basket')
]