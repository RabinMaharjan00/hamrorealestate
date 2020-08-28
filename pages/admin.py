from django.contrib import admin
from .models import CompanyInfo

# Register your models here.
class PagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')

admin.site.register(CompanyInfo, PagesAdmin)
