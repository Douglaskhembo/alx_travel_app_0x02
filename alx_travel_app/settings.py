import os
import environ
from pathlib import Path

# Base directory (MUST be above all os.path or env usage)
BASE_DIR = Path(__file__).resolve().parent

# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False)
)

# Load environment variables from .env in BASE_DIR
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Security settings
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Application definition
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'corsheaders',
    'drf_yasg',  # Swagger

    # Local apps
    'listings',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # must come before CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add paths like [BASE_DIR / "templates"] if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# Database using MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='3306'),
    }
}

AUTH_USER_MODEL = 'listings.CustomUser'


# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema',
}

# CORS configuration
CORS_ALLOW_ALL_ORIGINS = True  # For development only!
# In production, use:
# CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Chapa payment settings
CHAPA_SECRET_KEY = env('CHAPA_SECRET_KEY')

# Default admin user settings
DEFAULT_ADMIN_EMAIL = env('DEFAULT_ADMIN_EMAIL')
DEFAULT_ADMIN_PASSWORD = env('DEFAULT_ADMIN_PASSWORD')
DEFAULT_ADMIN_FIRST_NAME = env('DEFAULT_ADMIN_FIRST_NAME')
DEFAULT_ADMIN_LAST_NAME = env('DEFAULT_ADMIN_LAST_NAME')
DEFAULT_ADMIN_PHONE_NUMBER = env('DEFAULT_ADMIN_PHONE_NUMBER')

CELERY_BROKER_URL = env("CELERY_BROKER_URL")

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # for collectstatic

# Optional if you're serving additional static files manually
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

