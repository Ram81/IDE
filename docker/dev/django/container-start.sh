#!/bin/sh
cd /code && \
python manage.py migrate --noinput && \
python manage.py runserver 0.0.0.0:8000 & celery -A ide worker --app=ide.celery_app --loglevel=info
