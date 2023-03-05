from django.contrib import admin
from .models import Brand, Product, ProductVersion, ProductCategory, ProductImage, Property, PropertyOption, ProductReview
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductVersion)
# admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(Property)
admin.site.register(PropertyOption)
admin.site.register(Brand)


# 
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = ProductCategory.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = ProductCategory.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(ProductCategory, CategoryAdmin)
@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'rating', 'review')