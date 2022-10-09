$ heroku config:set DISABLE_COLLECTSTATIC=1
release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn water_sensor2.wsgi