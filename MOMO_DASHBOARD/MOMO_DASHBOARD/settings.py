"""
This file contains the settings for the MOMO_DASHBOARD project.

It was generated using Django 5.1.6 via the 'django-admin startproject' command.

You can learn more about this file at:
https://docs.djangoproject.com/en/5.1/topics/settings/

For comprehensive details on available settings and their respective values, refer to:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# Basic setup for development use only – not recommended for production environments
# Security recommendations and deployment guidelines:
# https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# Do not expose this secret key in a live production environment!
SECRET_KEY = 'django-insecure-n*4qb%r7)ctenya(g!i8c3ycb7(7e9hi@alj&4)vhsp)+vlxly'

# Enabling debug mode is unsafe for deployment. Use with caution.
DEBUG = True

# Define which hosts/domains the Django site can serve
ALLOWED_HOSTS = []


# Application configuration

INSTALLED_APPS = [
    'momo',  # Our custom application
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware configurations for handling requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Specifies the root URL configuration module
ROOT_URLCONF = 'MOMO_DASHBOARD.urls'

# Template engine settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add custom template directories here
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

# WSGI application reference
WSGI_APPLICATION = 'MOMO_DASHBOARD.wsgi.application'


# Database setup
# Learn more at: https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'momo_database.sqlite3',
    }
}


# Validators for user passwords
# Reference: https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Localization settings

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static file management (CSS, JS, images)
# See: https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'


# Default field type for auto-generated primary keys
# See more: https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
