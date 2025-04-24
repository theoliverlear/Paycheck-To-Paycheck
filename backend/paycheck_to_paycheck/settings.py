# settings.py
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / '.env')

SECRET_KEY = getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "ss-paycheck-to-paycheck.com",
    "www.ss-paycheck-to-paycheck.com",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'backend.paycheck_to_paycheck',
    'backend.apps',
    'backend',
    'backend.apps.entity',
    'backend.apps.entity.bill',
    'backend.apps.entity.holding',
    'backend.apps.entity.holding.debt',
    'backend.apps.entity.holding.saving',
    'backend.apps.entity.income',
    'backend.apps.entity.paycheck',
    'backend.apps.entity.tax',
    'backend.apps.entity.time',
    'backend.apps.entity.user',
    'backend.apps.entity.wallet',
    'backend.apps.routing',
    'livereload',
    'django_injector',
    'channels',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
    # 'backend.apps.injector.AppModule',
]
INJECTOR_MODULES = [
    'backend.apps.injector.AppModule',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
}

ROOT_URLCONF = 'backend.paycheck_to_paycheck.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://localhost:8001',
    'http://127.0.0.1:8001',
    "https://ss-paycheck-to-paycheck.com",
    "https://www.ss-paycheck-to-paycheck.com",
]

# SESSION_COOKIE_DOMAIN = "localhost"
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_NAME = "devsessionid"


CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "http://localhost:8001",
    "https://ss-paycheck-to-paycheck.com",
    "https://www.ss-paycheck-to-paycheck.com",
]
CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_ALL_ORIGINS = True

ASGI_APPLICATION = 'backend.paycheck_to_paycheck.asgi.application'
WSGI_APPLICATION = 'backend.paycheck_to_paycheck.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('PTP_DB_NAME'),
        'USER': getenv('PTP_DB_USER'),
        'PASSWORD': getenv('PTP_DB_PW'),
        'HOST': getenv('PTP_DB_HOST'),
        'PORT': '5432',

    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'