heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn water_sensor.asgi:application --port $PORT --bind 0.0.0.0 -v2
