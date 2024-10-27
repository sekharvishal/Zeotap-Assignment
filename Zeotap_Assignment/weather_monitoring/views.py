from django.shortcuts import render
from .models import WeatherData

def weather_summary(request):
    summaries = WeatherData.objects.all()
    return render(request, 'weather_summary.html', {'summaries': summaries})
