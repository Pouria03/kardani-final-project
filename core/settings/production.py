"""
    Use for proeuction
"""


from core.settings.base import *
import os


DEBUG = False
ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.{os.getenv('BACKEND_DB', 'mysql')}',
        'NAME': os.getenv('BACKEND_DB_NAME', 'name'),
        'HOST': os.getenv('BACKEND_DB_HOST', 'host'),
        'USER': os.getenv('BACKEND_DB_USER', 'user'),
        'PASSWORD': os.getenv('BACKEND_DB_PASS', 'password'),
        'PORT': os.getenv('BACKEND_DB_PORT', '5432')
    }
}



# django static root path
STATIC_ROOT = os.path.join(BASE_DIR, 'static')