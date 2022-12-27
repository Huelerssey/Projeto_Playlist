"""
urls from app music
"""
from django.urls import path
from .views import Homepage


app_name = 'musica'

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
]
