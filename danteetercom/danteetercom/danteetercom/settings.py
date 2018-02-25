"""
Django settings for danteetercom project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'danteeterwebsite@gmail.com'
EMAIL_HOST_PASSWORD = 'MyBlogIsTheBoss598*.'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'agk1in!q6_tk*4djv9flxtrj1y_2@@b#!us#sh3u509q#jg!-!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # APPS
    'blog',
    'contacts',
    'email_me',
    'shopping',
    'humancapital',
    'to_do_list',
    'hobbies',
    'timer',
    # PIP INSTALLS
    'import_export',
    'crispy_forms',
    'multiselectfield',
    'tinymce',
    'dajaxice',
    'dajax'
]

CRISPY_TEMPLATE_PACK = 'semantic-ui'
CRISPY_ALLOWED_TEMPLATE_PACKS = ('semantic-ui')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'danteetercom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'danteetercom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Pacific'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static ==============================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# MEDIA ==============================================
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"
