from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links =('id','name')

admin.site.register(Realtor)