from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import AbstractModel
# from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model

USER = get_user_model()



# Create your models here.
class BlogBanner(AbstractModel):
    image_large = models.ImageField(upload_to='blogBanner/', blank=True, null=True)


    class Meta:
        verbose_name = _('Blog_banner')
        verbose_name_plural = _('Blog_banners')


class Blog(AbstractModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=20000)
    # category = models.ManyToManyField('BlogCategory', related_name='blog_category', blank=True)
    image_small = models.ImageField(upload_to='blogPost/', blank=True, null=True)

    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


# class BlogCategory(AbstractModel):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = _('Blog Category')
#         verbose_name_plural = _('Blog Categories')