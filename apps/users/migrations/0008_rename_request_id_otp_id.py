# Generated by Django 4.2.4 on 2024-01-20 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_otp_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='request_id',
            new_name='id',
        ),
    ]
