# Generated by Django 4.2.4 on 2024-01-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_productgroup_remove_product_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroup',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
