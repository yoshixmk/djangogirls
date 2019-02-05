import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config()
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY']
