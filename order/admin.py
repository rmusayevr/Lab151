from django.contrib import admin
from .models import Basket, BasketItem, Wishlist, Order, OrderStatus, Address

# Register your models here.

admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Address)
