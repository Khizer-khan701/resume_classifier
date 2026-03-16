#!/bin/bash

# If FIREBASE_KEY_CONTENT is provided as an env variable, set it as FIREBASE_SERVICE_ACCOUNT_JSON
if [ ! -z "$FIREBASE_KEY_CONTENT" ]; then
    echo "Setting Firebase credentials from environment variable..."
    export FIREBASE_SERVICE_ACCOUNT_JSON="$FIREBASE_KEY_CONTENT"
fi

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create supervisor log directory
mkdir -p /var/log/supervisor

# Start Supervisor (Starts Redis, Django, and Celery)
exec supervisord -c /app/supervisor-hf.conf
