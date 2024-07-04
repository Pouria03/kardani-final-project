from pathlib import Path
from dotenv import load_dotenv, dotenv_values
import os


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY",
                       default='django-insecure-u8zf!$c2f1xp7acbkbhj7f$sit_kiz%7#b0-zn022m@)273)u#')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps :
    'blog_app',
    'home_app',
    'counseling_app',
    'about_app',
    'utils_app',
    # third party libraries
    'ckeditor',
    'ckeditor_uploader',
    'storages',
    'boto3',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = "core.wsgi.application"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'counseling_app.context_processors.counseling_types',
                # proj's custom context processors:
                'utils_app.context_processors.company_info',
            ],

        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


BASE_DOMAIN = os.getenv("BASE_DOMAIN",
                        default="localhost")


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEBUG = os.getenv('DEBUG', default='False')
ALLOWED_HOSTS = [] if DEBUG else ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3', # This is where you put the name of the db file. 
                    
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': f'django.db.backends.postgresql',
            'NAME': os.getenv('BACKEND_DB_NAME', default='name'),
            'HOST': os.getenv('BACKEND_DB_HOST', default='host'),
            'USER': os.getenv('BACKEND_DB_USER', default='user'),
            'PASSWORD': os.getenv('BACKEND_DB_PASS', default='password'),
            'PORT': os.getenv('BACKEND_DB_PORT', default=5432)
        }
    }


STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# uploads, use these if you have not implemented storage and boto3
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')


# ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"

if DEBUG:
    STATICFILES_DIRS = (
        # for local machine dubugging :
        (os.path.join(BASE_DIR, 'static')),
    )


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# storages
# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#     },
#     "staticfiles": {
#         "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
#     },
# }

# # S3 Settings
# LIARA_ENDPOINT = os.getenv("LIARA_ENDPOINT")
# LIARA_BUCKET_NAME = os.getenv("LIARA_BUCKET_NAME")
# LIARA_ACCESS_KEY = os.getenv("LIARA_ACCESS_KEY")
# LIARA_SECRET_KEY = os.getenv("LIARA_SECRET_KEY")

# # S3 Settings Based on AWS (optional)
# AWS_ACCESS_KEY_ID = LIARA_ACCESS_KEY
# AWS_SECRET_ACCESS_KEY = LIARA_SECRET_KEY
# AWS_STORAGE_BUCKET_NAME = LIARA_BUCKET_NAME
# AWS_S3_ENDPOINT_URL = LIARA_ENDPOINT
# AWS_S3_REGION_NAME = 'us-east-1'
