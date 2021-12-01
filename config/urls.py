# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    # main
    path('', include('apps.main.urls', namespace='main')),

    # admin
    path('admin/', admin.site.urls),
]
