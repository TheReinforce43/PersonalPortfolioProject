#!/bin/bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py loaddata core/fixtures/initial_data.json
python manage.py collectstatic --noinput