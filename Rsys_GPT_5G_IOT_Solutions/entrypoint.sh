#!/bin/bash

APP_PORT=${PORT:-8000}
cd /app/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm Rsys_GPT_5G_IOT_Solutions.wsgi:application --bind "0.0.0.0:${APP_PORT}"