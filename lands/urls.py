from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="lands"),
    path('<int:land_id>', views.land, name="land")
]
