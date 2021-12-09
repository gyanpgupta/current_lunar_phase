#!/bin/sh

set -e
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --no-input --username='admin'
uwsgi --socket :9000 --workers 4 --master --enable-threads --module backend.wsgi
