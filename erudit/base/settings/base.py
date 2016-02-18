"""
Django settings for erudit project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from unipath import Path

DEBUG = True
COMPRESS_ENABLED = True

BASE_DIR = Path(__file__)
ROOT_DIR = BASE_DIR.ancestor(4)

STATIC_ROOT = ROOT_DIR.child('static')
MEDIA_ROOT = ROOT_DIR.child('media')
UPLOAD_ROOT = MEDIA_ROOT.child('uploads')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

SECRET_KEY = 'INSECURE'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'modeltranslation',
    'post_office',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pipeline',
    'crispy_forms',
    'django_select2',
    'datetimewidget',
    'plupload',
    'django_filters',
    'spurl',
    'rules.apps.AutodiscoverRulesConfig',
    'ckeditor',

    # Érudit apps
    'base',
    'erudit',
    'apps.public.book',
    'apps.public.journal',
    'apps.public.search',
    'apps.public.thesis',
    'apps.userspace.dashboard',
    'apps.userspace.editor',
    'apps.userspace.individual_subscription',
    'apps.userspace.journal',
    'apps.userspace.permissions',
    'apps.userspace.subscription',
    'core.editor',
    'core.individual_subscription',
    'core.journal',
    'core.permissions',
    'core.subscription',
    'core.userspace',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zenon',
        'USER': 'postgres',
        'HOST': 'localhost',
    },
}

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_DIRS = (
    ROOT_DIR.child('erudit', 'static'),
)

PIPELINE = {
    'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
        # main css theme for erudit.org
        'erudit_main': {
            'source_filenames': (
                'sass/main.scss',
            ),
            'output_filename': 'css/main.min.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
        'pdfjs': {
            'source_filenames': (
                'vendor/pdfjs-build/generic/web/viewer.css',
                'sass/pages/_pdf_viewer.scss',
            ),
            'output_filename': 'css/pdfjs.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        # main js file for erudit.org
        'erudit_vendors': {
            # TODO : move this list in a common JS config file for Gulp and Pipeline
            'source_filenames': (
                'vendor/jquery/dist/jquery.js',
                'vendor/bootstrap-sass/assets/javascripts/bootstrap.js',
                'vendor/inline-svg/dist/inlineSVG.min.js',
            ),
            'output_filename': 'js/erudit-vendors.min.js',
        },
        'erudit_scripts': {
            'source_filenames': (
                'scripts/*.js',
                'scripts/modules/*.js',
                'scripts/sections/*.js',
            ),
            'output_filename': 'js/erudit-scripts.min.js',
        },
        'pdfjs': {
            'source_filenames': (
                'vendor/pdfjs-build/generic/web/compatibility.js',
                'vendor/pdfjs-build/generic/web/l10n.js',
                'vendor/pdfjs-build/generic/build/pdf.js',
                'vendor/pdfjs-build/generic/web/viewer.js',
            ),
            'output_filename': 'js/pdfjs.min.js',
        },
    }
}

# django-pipeline settings
PIPELINE['COMPILERS'] = (
    'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE['SASS_BINARY'] = '/usr/local/bin/sassc'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            ROOT_DIR.child('erudit', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'base.context_processors.common_settings',
            ],
        },
    },
]

LOGIN_URL = '/login/'

# Database configuration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

# Put this in settings.py
POST_OFFICE = {
    'DEFAULT_PRIORITY': 'now',
}

EMAIL_BACKEND = 'post_office.EmailBackend'
EMAIL_HOST = "mail"
EMAIL_PORT = '25'
RENEWAL_FROM_EMAIL = 'admin@localhost'
DEFAULT_FROM_EMAIL = 'ne-pas-repondre@erudit.org'

WSGI_APPLICATION = 'erudit.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr'

LANGUAGES = (
    ('fr', 'Français'),
    ('en', 'English'),
)

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


AUTHENTICATION_BACKENDS = [
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'base.backends.MandragoreBackend',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

INDIVIDUAL_SUBSCRIPTION_SALT = 'sample salt'

# Fedora settings
FEDORA_ROOT = 'http://10.1.1.33:8080/fedora/'
FEDORA_USER = 'fedoraAdmin'
FEDORA_PASSWORD = 'fedoraAdmin'

SOLR_ROOT = 'http://10.1.1.33:8080/solr/eruditpersee/'

try:
    from .settings_env import *  # noqa
except ImportError:
    pass

try:
    from ..settings_env import *  # noqa
except ImportError:
    pass
