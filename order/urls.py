from django.urls import path
from order.views import *

urlpatterns = [
    path('cart/', Cart.as_view(), name='cart'),
    path("test-payment/", test_payment_view, name="test-payment"),
    path("get-data-xml/", get_data_xml_view, name="get-data-xml"),
    path("payment/callback/", CallbackView.as_view(), name="payment-callback"),
]