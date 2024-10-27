from django.urls import path
from .views import weather_summary

urlpatterns = [
    path('summary/', weather_summary, name='weather_summary'),
]
