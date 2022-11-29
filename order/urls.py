from django.urls import path
from order.views import *

urlpatterns = [
    path('cart/', Cart.as_view(), name='cart'),
    path('api/basket/', BasketApiView.as_view(), name='api-basket')
]