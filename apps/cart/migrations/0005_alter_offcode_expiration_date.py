# Generated by Django 4.2.4 on 2024-01-10 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_offcode_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offcode',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 5, 56, 49, 696919), null=True),
        ),
    ]
