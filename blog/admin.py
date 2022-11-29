from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'author']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10

admin.site.register(BlogBanner)
# admin.site.register(BlogCategory)