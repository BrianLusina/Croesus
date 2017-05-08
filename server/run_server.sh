#!/usr/bin/env bash

# run celery worker
celery worker -A celery_worker.celery --loglevel=info
bg

# run application server
python3 manage.py runserver

