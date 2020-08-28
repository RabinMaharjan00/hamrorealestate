# Generated by Django 3.1 on 2020-08-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lands', '0007_auto_20200827_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='land',
            name='realtor',
        ),
        migrations.AddField(
            model_name='land',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='land',
            name='realtor_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='land',
            name='realtor_photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]