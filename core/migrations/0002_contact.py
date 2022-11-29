# Generated by Django 4.1.1 on 2022-11-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_src', models.TextField()),
                ('location', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]