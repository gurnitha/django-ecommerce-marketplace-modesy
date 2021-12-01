# apps/main/urls.py

# Django modules
from django.urls import path

# Locals
from apps.main import views

# App name
app_name = 'main'

urlpatterns = [
    
    # main
    path('', views.home, name='home'),
    
]
