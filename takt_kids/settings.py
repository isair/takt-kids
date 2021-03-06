"""
Django settings for takt_kids project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import dj_database_url

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Template directories
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )

# Required for Django suit
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('KIDS_DEBUG', 'true').lower() in ('true', 'yes', 't', 'y', '1')

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = '%g$7*j1f6^dd@m6o!e&bxfj&yoh6jk8ho$_zhzz8ptqp48gmyd'
else:
    SECRET_KEY = os.environ.get('KIDS_SECRET_KEY')

# Application definition
INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'boto',
    's3_folder_storage',
    'sorl.thumbnail',
    'easy_select2',
    'reversion',
    'social_auth',
    'main',
    'reception',
    'cosplay',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'takt_kids.urls'

WSGI_APPLICATION = 'takt_kids.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:////' + BASE_DIR + '/db.sqlite3')
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
if DEBUG:
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    MEDIA_ROOT = 'mediafiles'
    MEDIA_URL = '/media/'
else:
    DEFAULT_S3_PATH = 'media'
    STATIC_S3_PATH = 'static'

    AWS_ACCESS_KEY_ID = os.environ.get('KIDS_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('KIDS_AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = 'takt-kids'

    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'

    STATIC_ROOT = '/%s/' % STATIC_S3_PATH
    STATIC_URL = '//%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME

    MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
    MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Append slashes
APPEND_SLASH = True

# Grappelli configuration
GRAPPELLI_ADMIN_TITLE = 'TAKT - KIDS'

#Social auth configuration
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend'
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

if DEBUG:
    FACEBOOK_APP_ID = '284445315088366'
    FACEBOOK_API_SECRET = '702f4b84d9985756856b48d198e8ce4f'
else:
    FACEBOOK_APP_ID = os.environ.get('KIDS_FACEBOOK_APP_ID')
    FACEBOOK_API_SECRET = os.environ.get('KIDS_FACEBOOK_API_SECRET')
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['username', 'email']

LOGIN_REDIRECT_URL = '/reception'
