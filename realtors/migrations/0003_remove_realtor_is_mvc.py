# Generated by Django 3.1 on 2020-08-22 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_realtor_is_mvc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtor',
            name='is_mvc',
        ),
    ]
