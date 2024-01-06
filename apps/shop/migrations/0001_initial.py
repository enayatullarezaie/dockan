# Generated by Django 4.2.4 on 2024-01-05 17:12

import apps.shop.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('cover', models.FileField(null=True, upload_to='images/brand_cover/', validators=[apps.shop.models.validate_file_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('cover', models.FileField(null=True, upload_to='images/category_cover/', validators=[apps.shop.models.validate_file_extension])),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=256, null=True)),
                ('color', models.CharField(blank=True, max_length=256, null=True)),
                ('size', models.CharField(blank=True, max_length=256, null=True)),
                ('weight', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('count_in_stock', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cover', models.ImageField(upload_to='images/product_cover')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('rate', models.IntegerField(blank=True, default=0, null=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('dislikes', models.IntegerField(blank=True, default=0, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shop.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('image', models.FileField(null=True, upload_to='images/product_images/', validators=[apps.shop.models.validate_file_extension])),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
