from django.contrib import admin
from .models import Listing
from .models import Realtor

# Register your models here.
admin.site.register(Listing)
admin.site.register(Realtor)