$ heroku config:set DISABLE_COLLECTSTATIC=1
# release: python manage.py collectstatic
web: gunicorn water_sensor.wsgi:application --port $PORT --bind 0.0.0.0 -v2
