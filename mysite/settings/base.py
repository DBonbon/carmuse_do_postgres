"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from pathlib import Path
import os
import environ
import sys
import dj_database_url

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

env = environ.Env()
environ.Env.read_env()  # reading .env file
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',
    'search',

    'about',
    'blog',
    'catalog',
    'contact',
    'expo',
    'flex',
    'menus',
    'painter',
    'streams',

    'wagtail.contrib.forms',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.redirects',
    "wagtail.contrib.routable_page",
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',
    'django_extensions',
    'wagtailcaptcha',
    'wagtailfontawesome',
    'widget_tweaks',
    'wagtail_blocks',
    #'dbbackup',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'wagtailmenus.context_processors.wagtailmenus',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'
 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = "mysite"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'

# reCaptcha settings
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
RECAPTCHA_PUBLIC_KEY: '6Lc1cPMbAAAAAAd2S996JYEtBG2xXFwL3msYHxAt'
RECAPTCHA_PRIVATE_KEY: '6Lc1cPMbAAAAAO_94mWAv7keFlhRTWf8OQ1adWNo'
#RECAPTCHA_PUBLIC_KEY = '<your public reCaptcha key>'
#RECAPTCHA_PRIVATE_KEY = '<your private reCaptcha key>'
# enable no captcha
NOCAPTCHA = True

# Other
#DEFAULT_AUTO_FIELD='django.db.models.AutoField'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#DB BACKUPS
#DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'


#DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, '../backups')}