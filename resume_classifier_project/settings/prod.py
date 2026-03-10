from .base import *
import os

DEBUG = True

# Disable all middleware that could cause redirects
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ALLOWED_HOSTS = ['*']

# Absolute minimum proxy settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

# Explicitly disable all redirect-prone features
SECURE_SSL_REDIRECT = False
APPEND_SLASH = False
SECURE_HSTS_SECONDS = 0

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
