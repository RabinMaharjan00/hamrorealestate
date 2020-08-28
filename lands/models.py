from django.db import models
from datetime import datetime
from realtors.models import Realtor 

class Land(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    land_area = models.CharField(max_length=400)
    price = models.IntegerField()
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default= datetime.now, blank=True)
    def __str__(self):
        return self.title

