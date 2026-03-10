from .base import *
import os

DEBUG = True

# Disable almost everything for deep diagnostics
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ALLOWED_HOSTS = ['*']

# Explicitly handle Hugging Face Proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# Kill all internal redirects
SECURE_SSL_REDIRECT = False
APPEND_SLASH = False
PREPEND_WWW = False

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
