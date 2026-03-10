from .base import *
import os

DEBUG = True  # Temporarily enabled to see the actual error

ALLOWED_HOSTS = ['*']

# We are using sqlite3 for basic Django requirements
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Simplified Security (Disabled for debugging)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0
SECURE_CONTENT_TYPE_NOSNIFF = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'ALLOWALL' # Help with HF iframe
