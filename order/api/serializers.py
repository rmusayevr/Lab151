from rest_framework import serializers
from order.models import Basket, BasketItem
from products.api.serializers import ProductVersionListSerializer

class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = [
            'user',
            'items'
        ]

class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductVersionListSerializer()

    class Meta:
        model = BasketItem
        fields = [
            'user',
            'product', 
            'quantity'
        ]