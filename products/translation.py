from modeltranslation.translator import register, TranslationOptions
from .models import ProductCategory


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'parent')