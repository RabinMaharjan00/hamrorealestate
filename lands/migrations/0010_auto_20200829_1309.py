# Generated by Django 3.1 on 2020-08-29 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0009_auto_20200827_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='land',
            old_name='price',
            new_name='price_per_anna',
        ),
    ]
