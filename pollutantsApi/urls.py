"""pollutantsApi URL Configuration
"""
from django.contrib import admin
from django.urls import path
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', api_views.get_readings, name="readings"),
]
