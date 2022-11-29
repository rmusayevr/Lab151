# Generated by Django 4.1.1 on 2022-11-28 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0004_alter_basketitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_basket_item', to=settings.AUTH_USER_MODEL),
        ),
    ]