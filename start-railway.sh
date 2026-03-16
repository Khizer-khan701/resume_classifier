#!/bin/bash

# If FIREBASE_KEY_CONTENT is provided as an env variable, write it to the file
if [ ! -z "$FIREBASE_KEY_CONTENT" ]; then
    echo "Writing Firebase key from environment variable..."
    echo "$FIREBASE_KEY_CONTENT" > /app/firebase-key.json
fi

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create supervisor log directory
mkdir -p /var/log/supervisor

# Start Supervisor (Starts Django and Celery)
exec supervisord -c /app/supervisor-railway.conf