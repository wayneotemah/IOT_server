$ export DJANGO_SETTINGS_MODULE=water_sensor2.settings
$ heroku config:set DJANGO_SETTINGS_MODULE=water_sensor2.settings
$ heroku config:set DISABLE_COLLECTSTATIC=1
release: python manage.py migrate
web: gunicorn water_sensor2.wsgi