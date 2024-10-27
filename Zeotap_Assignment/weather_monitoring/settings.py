CELERY_BROKER_URL = 'redis://localhost:6379/0'  # 
from celery.schedules import crontab # type: ignore

CELERY_BEAT_SCHEDULE = {
    'fetch-weather-every-5-minutes': {
        'task': 'Weather_Monitering.tasks.fetch_weather_data',  # 
        'schedule': crontab(minute='*/5'),  # Every 5 minutes
    },
}
