# Generated by Django 4.2.4 on 2024-01-20 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_shippingaddress'),
        ('cart', '0008_cartitem_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addresses', to='users.shippingaddress'),
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
