#!/bin/bash

# Apply database migrations (SQLite on Render will reset on deploy, but needed for startup)
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create supervisor log directory
mkdir -p /var/log/supervisor

# Start Supervisor
exec supervisord -c /app/supervisor-render.conf
