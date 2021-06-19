
import os
from .base  import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l5ocyes_)eqnkq7sllpp&ks0*&xa$3f+scrsbp!qyg1r77(h6!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]



# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online_study_db',
        'USER': 'ccq',
        'PASSWORD': 'test123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


