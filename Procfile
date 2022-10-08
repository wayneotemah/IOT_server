$ heroku config:set DISABLE_COLLECTSTATIC=1
# release: python manage.py collectstatic
web: gunicorn water_sensor.wsgi:application
