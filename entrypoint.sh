#!/bin/bash

./wait-for-it.sh mysql:3306
python manage.py collectstatic --no-input
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8000
