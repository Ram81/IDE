#!/bin/sh
cd /code && \
python manage.py makemigrations caffe_app && \
python manage.py migrate --noinput && \
python manage.py collectstatic --noinput
uwsgi --ini /code/docker/prod/django/uwsgi.ini & daphne -b 0.0.0.0 -p 8001 ide.asgi:channel_layer
