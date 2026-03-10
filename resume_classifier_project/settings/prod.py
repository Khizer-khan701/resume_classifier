from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['*']

# CSRF Trusted Origins for Hugging Face
CSRF_TRUSTED_ORIGINS = [
    'https://*.hf.space',
    'https://*.huggingface.co'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', # Static files first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middleware.GlobalErrorHandlingMiddleware',
]

# Hugging Face Proxy Settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# Disable ALL automated redirects
SECURE_SSL_REDIRECT = False
APPEND_SLASH = False # Kill trailing slash redirects
REMOVE_SLASH = False
SECURE_HSTS_SECONDS = 0

# Cookie settings for Hugging Face iFrames
# SESSION_COOKIE_SAMESITE = 'None' # Requires SECURE=True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SAMESITE = 'None'
# CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
