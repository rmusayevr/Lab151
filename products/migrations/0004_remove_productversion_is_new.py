# Generated by Django 4.1.1 on 2022-09-26 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_brand_productcategory_parent_alter_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productversion',
            name='is_new',
        ),
    ]
