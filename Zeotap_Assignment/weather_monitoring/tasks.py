
from celery import shared_task
import requests
from .models import WeatherData
from django.utils import timezone

@shared_task
def fetch_weather_data():
    api_key = "your_openweathermap_api_key"
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    for city in cities:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric')
        data = response.json()
        weather = WeatherData.objects.create(
            city=city,
            main_condition=data['weather'][0]['main'],
            temp=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            recorded_at=timezone.now()
        )
    return "Weather data fetched successfully."
