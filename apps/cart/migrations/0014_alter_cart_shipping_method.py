# Generated by Django 4.2.4 on 2024-01-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_cart_shipping_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='shipping_method',
            field=models.IntegerField(default=30000),
        ),
    ]
