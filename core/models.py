from statistics import mode
from django.db import models

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Slider(models.Model):
    slider = models.ImageField(upload_to = "Slider Images")

    class Meta:
        verbose_name = "Slider Image"
        verbose_name_plural = "Slider Images"
        

class Banner(models.Model):
    banner_small1 = models.ImageField(upload_to = "Banner Images1", null = True)
    banner_small2 = models.ImageField(upload_to = "Banner Images2", null = True)
    banner_small3 = models.ImageField(upload_to = "Banner Images3", null = True)
    banner_small4 = models.ImageField(upload_to = "Banner Images4", null = True)

    class Meta:
        verbose_name = "Banner Image"
        verbose_name_plural = "Banner Images"

class Contact(models.Model):
    location_src = models.TextField()
    location = models.TextField()
    phone = models.CharField(max_length=15)
    mail = models.EmailField()