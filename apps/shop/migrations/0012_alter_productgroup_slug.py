# Generated by Django 4.2.4 on 2024-01-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_productgroup_slug_alter_productgroup_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroup',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=256, null=True, unique=True),
        ),
    ]
