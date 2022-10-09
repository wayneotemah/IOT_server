$ export DJANGO_SETTINGS_MODULE=water_sensor2.settings
$ heroku config:set DJANGO_SETTINGS_MODULE=water_sensor2.settings
$ heroku config:set DISABLE_COLLECTSTATIC=1
release: manage.py migrate
web: gunicorn water_sensor2.asgi:application --port $PORT --bind 0.0.0.0 -v2
