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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'HOST': 'mysql',
        'USER': 'mysql',
        'PASSWORD': 'mysql',
    }
}



# django static root path
STATIC_ROOT = os.path.join(BASE_DIR, 'static')