release: python manage.py collectstatic
web: daphne water_sensor.asgi:application --port $PORT --bind 0.0.0.0 -v2
