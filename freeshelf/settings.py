"""
Django settings for freeshelf project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.contrib.messages import constants as messages
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
    # 'MEDIA_ROOT' defined as the full path directory where you'd like Django to store uploaded files
MEDIA_URL = '/media/'
    # 'MEDIA_URL' defined as the base public URL of that directory


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')crne*aq^_jn==5)!6@)$zcc9+g+o)cn@+g!qcma$64(jxw-az'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 3rd-party apps that should come before 'django.contrib.admin'
    'registration',

    # built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
        # Core authentication framework and its default models
    'django.contrib.contenttypes',
        # Django content type system (allows permissions to be associated with models)
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
        # added 3/14/19 for django-registration-redux
        # this broke my login site, so commented it out and it worked

    # my apps
    # 'freeshelfapp.apps.FreeshelfappConfig', # MDN tutorial way and it works
    'freeshelfapp', # Clinton's way and it works as well

    # 3rd-party apps
    'debug_toolbar',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
        # Manages sessions across requests
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
        # Associates users with requests using sessions
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'freeshelf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
            # makes the templates directory visible to the template loader
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'freeshelf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York' # default 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'

# Registration
ACCOUNT_ACTIVATION_DAYS = 7
    # One-week activation window
LOGIN_REDIRECT_URL = '/'
    # Redirect to home URL after login (Default redirects to /accounts/profile/)

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # Logs any emails sent to the console (so the password reset link can be copied from the console for testing)

# Messages
MESSAGE_TAGS = {
    messages.INFO: 'b--blue bg-light-blue',    
    messages.SUCCESS: 'b--green bg-light-green'
        # styles messages used through-out the project
}

django_heroku.settings(locals())
    # locals returns a dictionary of all your local variables