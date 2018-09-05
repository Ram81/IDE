#!/bin/sh
cd /code && \
python manage.py migrate --noinput && \
python manage.py collectstatic --noinput
uwsgi --ini /code/docker/prod/django/uwsgi.ini
