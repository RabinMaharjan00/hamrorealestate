from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=setting.MEDIA_ROOT)
