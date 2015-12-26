import os
from .common import *

BASE_DIR = os.environ['DATA_DIR']

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'site.db'),
    },
}

SECRET_KEY = os.getenv('SECRET_KEY')
