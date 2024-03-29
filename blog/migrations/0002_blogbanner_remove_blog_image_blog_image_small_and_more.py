# Generated by Django 4.1.1 on 2022-09-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_large', models.ImageField(blank=True, null=True, upload_to='blogBanner/')),
            ],
            options={
                'verbose_name': 'Blog_banner',
                'verbose_name_plural': 'Blog_banners',
            },
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='image_small',
            field=models.ImageField(blank=True, null=True, upload_to='blogPost/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=20000),
        ),
    ]
