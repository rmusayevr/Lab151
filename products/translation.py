from modeltranslation.translator import register, TranslationOptions
from .models import ProductCategory, Product


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'parent')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')