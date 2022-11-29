from rest_framework import serializers
from .models import Product, ProductCategory, ProductVersion, Brand
from math import ceil


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'name',
            'parent',
        )

# class BrandListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brand
#         fields = (
#             'id',
#             'name',
#         )

class ProductListSerializer(serializers.ModelSerializer):
    # brand = BrandListSerializer(many=True)
    category = CategoryListSerializer(many=True)
    real_price = serializers.SerializerMethodField()
    visual_price = serializers.SerializerMethodField()
    visual_cover_image = serializers.SerializerMethodField()
    visual_cover_image_2 = serializers.SerializerMethodField()
    star_ratings = serializers.SerializerMethodField()
    is_sale = serializers.SerializerMethodField()
    detail_url = serializers.SerializerMethodField()
    
    def get_real_price(self, obj):
        return obj.get_visual_product.price

    def get_visual_price(self, obj):
        return obj.get_visual_product.get_price

    def get_visual_cover_image(self, obj):
        return obj.get_visual_product.cover_image.url

    def get_visual_cover_image_2(self, obj):
        if obj.get_visual_product.cover_image_2:
            return obj.get_visual_product.cover_image_2.url

    def get_star_ratings(self, obj):
        sum = 0
        for review in obj.product_reviews.all():
            sum += review.rating
        rating = (ceil(sum / obj.product_reviews.count())
                  ) if obj.product_reviews.count() > 0 else 0
        return rating

    def get_is_sale(self, obj):
        return obj.get_visual_product.is_sale
    
    def get_detail_url(self, obj):
        return obj.get_absolute_url()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'category',
            'brand',
            'real_price',
            'visual_price',
            'visual_cover_image',
            'visual_cover_image_2',
            'star_ratings',
            'is_sale',
            'detail_url'
        )


class ProductVersionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVersion
        fields = (
            'id',
            'product',
            'cover_image',
            'cover_image_2',
            'price',
            'quantity',
            'code',
            'property_options',
            'is_sale',
            'is_stock',
            'sale_percent',
        )
    
