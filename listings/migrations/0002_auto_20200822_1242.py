# Generated by Django 3.1 on 2020-08-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
