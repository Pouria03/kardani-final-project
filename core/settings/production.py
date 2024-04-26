"""
    Use for proeuction
"""


from core.settings.base import *
import os


DEBUG = False
ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# django static root path
STATIC_ROOT = os.path.join(BASE_DIR, 'static')