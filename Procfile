$ heroku config:set DISABLE_COLLECTSTATIC=1
# release: python manage.py collectstatic
web: daphne water_sensor2.asgi:application --port $PORT --bind 0.0.0.0 v2
