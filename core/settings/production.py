"""
    Use for production
"""


from core.settings.base import *
import os


DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1'] # add the remote domain to the list like 'x.pythonanywhere.com'
# CSRF_TRUSTED_ORIGINS = ['https://x.pythonanywhere.com'] # uncomment this and add your remote domain



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

