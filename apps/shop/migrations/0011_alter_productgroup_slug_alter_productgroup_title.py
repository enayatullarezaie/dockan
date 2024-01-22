# Generated by Django 4.2.4 on 2024-01-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_productgroup_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroup',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='title',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
