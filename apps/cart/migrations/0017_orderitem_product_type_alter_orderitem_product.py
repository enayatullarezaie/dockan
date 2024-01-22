# Generated by Django 4.2.4 on 2024-01-22 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_productgroup_slug'),
        ('cart', '0016_rename_address_cart_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product_type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.producttype'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product'),
        ),
    ]
