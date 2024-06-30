from pathlib import Path

import os


BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY",
                        'django-insecure-u8zf!$c2f1xp7acbkbhj7f$sit_kiz%7#b0-zn022m@)273)u#')


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
                        "localhost")


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEBUG = os.getenv('DEBUG', 'True')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', ['*', ])

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': f'django.db.backends.postgresql',
            'NAME': os.getenv('BACKEND_DB_NAME', 'name'),
            'HOST': os.getenv('BACKEND_DB_HOST', 'host'),
            'USER': os.getenv('BACKEND_DB_USER', 'user'),
            'PASSWORD': os.getenv('BACKEND_DB_PASS', 'password'),
            'PORT': os.getenv('BACKEND_DB_PORT', '5432')
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }



STATIC_URL = 'static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# uploads
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
