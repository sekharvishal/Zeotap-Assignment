# Real-Time Weather Monitoring System

## Overview
The Real-Time Weather Monitoring System is a Django application designed to monitor and display real-time weather data for several major cities in India. By leveraging the OpenWeatherMap API, this application retrieves weather information at regular intervals, providing users with up-to-date summaries of conditions such as temperature and weather status. The system uses Celery for background task management, allowing it to fetch data every five minutes seamlessly.

## Features
This application offers a range of features including automatic fetching of weather data, which is updated every five minutes. Users can view comprehensive weather summaries that display essential information like the current temperature, perceived temperature, main weather conditions, and the time of data retrieval. The user interface is built using Django templates, ensuring a clean and responsive design. Additionally, the application can be easily extended to include more weather parameters and alerts based on user-defined thresholds.

## Prerequisites
To run this application, ensure you have Python 3.x installed, along with Django version 3.x or higher. You will also need Redis or another message broker to manage Celery tasks. Lastly, sign up for an API key from OpenWeatherMap to access the weather data.

## Installation
To get started, clone the repository using `git clone https://github.com/yourusername/weather_monitoring.git`, then navigate into the project directory. Create a virtual environment with `python -m venv venv` and activate it. After activating the environment, install the required packages listed in `requirements.txt`. Update the `settings.py` file with your database configuration, and run `python manage.py migrate` to set up the database schema. Don’t forget to replace `"your_openweathermap_api_key"` in `tasks.py` with your actual API key.

## Running the Application
To run the application, start the Django development server with `python manage.py runserver`. If you're using Redis or another message broker, make sure it is running. Next, start the Celery worker by executing `celery -A your_project_name worker -l info`, followed by starting Celery Beat for periodic tasks with `celery -A your_project_name beat -l info`. You can then visit `http://127.0.0.1:8000/summary/` in your web browser to view the daily weather summaries.

## Usage
The application automatically fetches weather data every five minutes, and users can refresh the summary page to see the latest updates. This makes it easy to monitor changing weather conditions in real-time.

## Testing
For testing purposes, you can manually trigger the `fetch_weather_data` task from the Django shell or set breakpoints to ensure that data is being fetched and stored correctly in the database.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality and features of this application.

## License
This project is licensed under the MIT License. For more details, please refer to the LICENSE file.

## Acknowledgments
This application utilizes several technologies, including Django for web development, Celery for background task processing, and the OpenWeatherMap API for accessing weather data. We extend our gratitude to these projects for their valuable resources.
