from django.contrib import admin
from .models import Brand, Product, ProductVersion, ProductCategory, ProductImage, Property, PropertyOption, ProductReview

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductVersion)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(Property)
admin.site.register(PropertyOption)

admin.site.register(Brand)

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'rating', 'review')