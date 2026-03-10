from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# We are using sqlite3 for basic Django requirements (Admin, Sessions, ContentTypes)
# App-specific data is stored in Firestore.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
