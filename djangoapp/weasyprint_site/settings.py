"""
Django settings for weasyprint_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    from local_settings import *
except ImportError as e:
    pass
    
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%9quoc(^@5mh-2%w#^dpdh@ay3t1wfpa6kin7)urhn5r1p2klo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jinja',
    'reports',
    'weasyprint'
)

TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
)

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'

# Same behavior of default intercept method
# by extension but using regex (not recommended)
DEFAULT_JINJA2_TEMPLATE_INTERCEPT_RE = r'.*jinja$'

# More advanced method. Intercept all templates
# except from django admin.
DEFAULT_JINJA2_TEMPLATE_INTERCEPT_RE = r"^(?!admin/).*"

JINJA2_ENVIRONMENT_OPTIONS = {
    'block_start_string' : '\BLOCK{',
    'block_end_string' : '}',
    'variable_start_string' : '\VAR{',
    'variable_end_string' : '}',
    'comment_start_string' : '\#{',
    'comment_end_string' : '}',
    'line_statement_prefix' : '%-',
    'line_comment_prefix' : '%#',
    'trim_blocks' : True,
    'autoescape' : False,
}

# Enable/Disable autoescaping (default: True)
JINJA2_AUTOESCAPE = True

# Mute reverse url exceptions (default: False)
JINJA2_MUTE_URLRESOLVE_EXCEPTIONS = True

# Keep original small subset of jinja filters
# instead of use the django's versions of them.
# Default: True
JINJA2_FILTERS_REPLACE_FROM_DJANGO = False

# Enable bytecode cache (default: False)
JINJA2_BYTECODE_CACHE_ENABLE = False

# Cache backend name for bytecode cache (default: "default")
JINJA2_BYTECODE_CACHE_NAME = "default"

# Specify custom bytecode cache subclass (default: None)
# JINJA2_BYTECODE_CACHE_BACKEND = "path.to.you.cache.class"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'weasyprint_site.urls'

WSGI_APPLICATION = 'weasyprint_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# user-generated content 
MEDIA_URL = '/media/'

# typically 
# need this for production environment
STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'www', 'media')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'weasyprint_site/debug.log',
        },
    },
    'loggers': {
        'reports.admin' : {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
