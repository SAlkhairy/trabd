"""
Django settings for trabd project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import secrets
from django.core.urlresolvers import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getattr(secrets, 'DEBUG', False)

ALLOWED_HOSTS = ['127.0.0.1', '.trabdportal.com']

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'loginas',
    'bootstrap3',
    'voting',
    'accounts',
    'userena',
    'general',
    'guardian',
    'easy_thumbnails',
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

ROOT_URLCONF = 'trabd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'voting.context_processors.sac_year',
            ],
        },
    },
]

WSGI_APPLICATION = 'trabd.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DEFAULT_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = getattr(secrets, 'DATABASES', DEFAULT_DATABASES)

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
else:
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# Email settings
EMAIL_BACKEND = getattr(secrets, 'EMAIL_BACKEND', 'django.core.mail.backends.dummy.EmailBackend')
DEFAULT_FROM_EMAIL = 'noreply@trabdportal.com'
EMAIL_USE_TLS = getattr(secrets, 'EMAIL_USE_TLS', True)
EMAIL_HOST = getattr(secrets, 'EMAIL_HOST', '')
EMAIL_PORT = getattr(secrets, 'EMAIL_PORT', 0)
EMAIL_HOST_USER = getattr(secrets, 'EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = getattr(secrets, 'EMAIL_HOST_PASSWORD', '')
SERVER_EMAIL = 'errors@trabdportal.com'
ADMINS = [('Errors', 'errors@trabdportal.com')]

# Userena settings
SITE_ID = 1
ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'accounts.Profile'
USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/' #Bad hardcoding but I dont know how to fix it right now
LOGIN_URL = reverse_lazy('userena_signin')
LOGOUT_URL = reverse_lazy('loginas-logout')
LOGINAS_LOGOUT_REDIRECT_URL = reverse_lazy('home')
LOGIN_REDIRECT_URL = USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGOUT_REDIRECT_URL = USERENA_REDIRECT_ON_SIGNOUT = reverse_lazy('home')

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ar-SA'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = getattr(secrets, 'STATIC_URL', '/static/')
DEFAULT_STATIC_ROOT = os.path.join(BASE_DIR, 'static_files/')
STATIC_ROOT = getattr(secrets, 'STATIC_ROOT', DEFAULT_STATIC_ROOT)
MEDIA_URL = getattr(secrets, 'MEDIA_URL', '/media/')
DEFAULT_MEDIA_ROOT = os.path.join(BASE_DIR, 'media_files/')
MEDIA_ROOT = getattr(secrets, 'MEDIA_ROOT', DEFAULT_MEDIA_ROOT)

# Security settings
SECURE_HSTS_SECONDS = getattr(secrets, 'SECURE_HSTS_SECONDS', 0)
SESSION_COOKIE_DOMAIN = getattr(secrets, 'SESSION_COOKIE_DOMAIN', None)
CSRF_COOKIE_DOMAIN = getattr(secrets, 'CSRF_COOKIE_DOMAIN', None)
