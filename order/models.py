from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AbstractModel
from django.contrib.auth import get_user_model

USER = get_user_model()


# Create your models here.

class Basket(AbstractModel):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='basket')
    items = models.ManyToManyField('BasketItem', related_name='basket_items', blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')


class BasketItem(AbstractModel):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, null=True, blank=True, related_name="user_basket_item")
    product = models.ForeignKey('products.ProductVersion', on_delete=models.CASCADE, related_name='basket_product')
    quantity = models.IntegerField(default=0)

    def get_subtotal(self):
        if self.product.is_sale:
            subtotal = self.product.get_price*self.quantity
        else:
            subtotal = self.product.price*self.quantity
        return subtotal
        
    def __str__(self):
        return self.product.product.title

    class Meta:
        verbose_name = _('Basket Item')
        verbose_name_plural = _('Basket Items')


class Wishlist(AbstractModel):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='wishlist')
    productversion = models.ManyToManyField('products.ProductVersion', related_name='wishlist_productversion', blank=True)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Wishlist')
        verbose_name_plural = _('Wishlists')


class Order(AbstractModel):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='order')
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE, related_name='order_basket')
    status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, related_name='order_status')
    # payment = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='order_payment')
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='order_address')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderStatus(AbstractModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Order Status')
        verbose_name_plural = _('Order Statuses')


class Address(AbstractModel):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='address')
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')