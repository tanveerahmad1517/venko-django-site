import os
from openshiftlibs import openshift_secure

DATA_DIR = os.environ['OPENSHIFT_DATA_DIR']
REPO_DIR = os.environ['OPENSHIFT_REPO_DIR']
WWW_ROOT = os.path.join(REPO_DIR, 'wsgi/')

STATIC_ROOT = os.path.join(WWW_ROOT, 'static/')
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media/')

STATIC_URL = '/static/'
MEDIA_URL = os.path.join(STATIC_URL, 'media/')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '*',
]

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'site.db'),
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['OPENSHIFT_APP_NAME'],
        'USER': os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
        'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
        'HOST': os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
        'PORT': os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
    }
}
DATABASES['default'] = DATABASES['postgres']

DISQUS_WEBSITE_SHORTNAME = 'venelin'

SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'webmaster@venelin.sytes.net'

SECRET_KEY = openshift_secure('qi!k%l+n@hs8l8%)t@j2bl6_jj_x2q-g^em=i!6m17(7x1^$9r')
