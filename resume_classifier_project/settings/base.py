import os
from pathlib import Path
from dotenv import load_dotenv
import json

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-^o=up#*r^krnxelq5scoz)tr-cpv5yazg6hdq0a_oc8*12)&f5')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party
    'rest_framework',
    
    # Local apps
    'accounts',
    'resumes',
    'ai_analysis',
    'jobs',
    'reports',
    'dashboard',
    'common',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middleware.GlobalErrorHandlingMiddleware',
]

ROOT_URLCONF = 'resume_classifier_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.user_profile',
            ],
        },
    },
]

WSGI_APPLICATION = 'resume_classifier_project.wsgi.application'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'accounts.auth_backend.FirebaseAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'dashboard:home'
LOGOUT_REDIRECT_URL = 'accounts:login'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files setup for local development. We will provide an abstraction in resumes module.
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --- Firebase & Firestore Configuration ---
import firebase_admin
from firebase_admin import credentials

# Initialize Firebase credentials
firebase_cred = None

# First, try to load from environment variable (for Railway/production)
firebase_json_str = os.environ.get('FIREBASE_SERVICE_ACCOUNT_JSON')
if firebase_json_str:
    try:
        firebase_dict = json.loads(firebase_json_str)
        firebase_cred = credentials.Certificate(firebase_dict)
        print("Firebase credentials loaded from FIREBASE_SERVICE_ACCOUNT_JSON environment variable.")
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse FIREBASE_SERVICE_ACCOUNT_JSON: {e}")
    except Exception as e:
        print(f"ERROR: Failed to initialize Firebase from env var: {e}")
else:
    # Fallback to file-based credentials (for local development)
    env_path = os.environ.get('FIREBASE_CREDENTIALS_PATH')
    docker_path = '/app/firebase-key.json'
    local_path = 'firebase_key.json'

    FIREBASE_CREDENTIALS_PATH = None
    if env_path and os.path.exists(env_path):
        FIREBASE_CREDENTIALS_PATH = env_path
    elif os.path.exists(docker_path):
        FIREBASE_CREDENTIALS_PATH = docker_path
    elif os.path.exists(local_path):
        FIREBASE_CREDENTIALS_PATH = local_path

    if FIREBASE_CREDENTIALS_PATH:
        try:
            firebase_cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
            print(f"Firebase credentials loaded from file: {FIREBASE_CREDENTIALS_PATH}")
        except Exception as e:
            print(f"ERROR: Failed to load Firebase credentials from file {FIREBASE_CREDENTIALS_PATH}: {e}")
    else:
        print("WARNING: Firebase credentials not found. Firestore features will be disabled.")

# Initialize Firebase if credentials are available
if firebase_cred and not firebase_admin._apps:
    try:
        firebase_admin.initialize_app(firebase_cred)
        print("Firebase Admin SDK initialized successfully.")
    except Exception as e:
        print(f"ERROR: Failed to initialize Firebase Admin SDK: {e}")
elif not firebase_cred:
    print("WARNING: Firebase credentials file not found. Firestore features will be disabled.")


# --- Redis & Celery Configuration ---
REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_BROKER_CONNECTION_TIMEOUT = 10  # Shorter timeout to avoid hanging runserver
CELERY_BROKER_CONNECTION_RETRY_ON_START = True


# --- LangChain & LLM Configuration ---
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
