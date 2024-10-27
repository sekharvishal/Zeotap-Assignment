from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    main_condition = models.CharField(max_length=100)
    temp = models.FloatField()  # Temperature in Celsius
    feels_like = models.FloatField()
    recorded_at = models.DateTimeField()

    class Meta:
        ordering = ['-recorded_at']
