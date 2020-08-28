from django.contrib import admin
from .models import Land

# Register your models here.
class LandAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'address', 'city', 'list_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title','description', 'address', 'city','price')
    list_per_page = 25


admin.site.register(Land, LandAdmin)