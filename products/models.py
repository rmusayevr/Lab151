from xmlrpc.client import Boolean
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AbstractModel
from math import ceil
from django.urls import reverse
# from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

# Create your models here.
class ProductCategory(MPTTModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    parent = TreeForeignKey('self', related_name="children", blank=True,
                            null=True, on_delete=models.CASCADE, verbose_name="Üst Kateqoriya")
  
    def __str__(self):
        return self.name

    class MPTTMeta:
            order_insertion_by = ['name']

   

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')

class Product(AbstractModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(
        max_length=20000, verbose_name=_('Description'))
    category = models.ForeignKey(
        'ProductCategory', related_name='product_categories',on_delete=models.CASCADE,  blank=True, verbose_name=_('Category'))
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE,
                              related_name='brand_products', verbose_name=_('Brand'), null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={"pk": self.pk})

    @property
    def get_star_ratings(self):
        sum = 0
        for review in self.product_reviews.all():
            sum += review.rating
        rating = (ceil(sum / self.product_reviews.count())
                  ) if self.product_reviews.count() > 0 else 0
        return range(rating)

    @property
    def get_nonstar_ratings(self):
        sum = 0
        for review in self.product_reviews.all():
            sum += review.rating
        rating = (ceil(sum / self.product_reviews.count())
                  ) if self.product_reviews.count() > 0 else 0
        return range(5 - rating)

    @property
    def get_visual_product(self):
        for version in self.product_version.all():
            if version.is_stock:
                return version

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductVersion(AbstractModel):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='product_version', verbose_name=_('Product'))
    cover_image = models.ImageField(
        upload_to='product_version/', blank=True, null=True, verbose_name=_('Cover Image'))
    cover_image_2 = models.ImageField(
        upload_to='product_version/', blank=True, null=True, verbose_name=_('Cover Image 2'))
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_('Price'))
    quantity = models.IntegerField(default=1, verbose_name=_('Quantity'))
    code = models.BigIntegerField(
        default=0000000000000, verbose_name=_('Code'))
    property_options = models.ManyToManyField(
        'PropertyOption', related_name='product_property_options', blank=True, verbose_name=_('Property Options'))
    is_stock = models.BooleanField(default=True, verbose_name=_('Is Stock'))
    is_sale = models.BooleanField(default=False, verbose_name=_('Is Sale'))
    sale_percent = models.IntegerField(
        default=0, verbose_name=_('Sale Percent'))
    final_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_('Final Price'))

    def __str__(self):
        return self.product.title + ' ' + str(self.id)

    @property
    def get_price(self):
        if self.is_sale:
            self.final_price = self.price
            return self.price - (self.price * self.sale_percent / 100)
        return self.price

    def save(self, *args, **kwargs):
        if self.is_sale:
            self.final_price = self.price - (self.price * self.sale_percent / 100)
            return super().save()
        self.final_price = self.price
        return super().save()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Product Version')
        verbose_name_plural = _('Product Versions')





class ProductImage(AbstractModel):
    product_version = models.ForeignKey(
        'ProductVersion', on_delete=models.CASCADE, related_name='product_image', verbose_name=_('Product Version'))
    image = models.ImageField(
        upload_to='product_image/', blank=True, null=True, verbose_name=_('Image'))

    def __str__(self):
        return self.product_version.product.title + ' - ' + str(self.id)

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')


class Property(AbstractModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')


class PropertyOption(AbstractModel):
    property = models.ForeignKey(
        'Property', on_delete=models.CASCADE, related_name='property_option', verbose_name=_('Property'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __str__(self):
        return f'{self.property.name} - {self.name}'

    class Meta:
        verbose_name = _('Property Option')
        verbose_name_plural = _('Property Options')


class ProductReview(AbstractModel):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='product_reviews', verbose_name=_('Product'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    review = models.TextField(verbose_name=_('Review'))
    rating = models.IntegerField(default=5, verbose_name=_('Rating'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Review')
        verbose_name_plural = _('Product Reviews')


class Brand(AbstractModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    slug = models.SlugField(max_length=255, verbose_name=_('Slug'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')
