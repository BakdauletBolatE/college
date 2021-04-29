
try:
    from .local_settings import *
    DEBUG = True
except ImportError as e:
    DEBUG = False

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8rp&j5jfqdi-spuqv-)!g%erfdw2qzizrp_h0keouv$0+391f('



if DEBUG:
    ALLOWED_HOSTS = ['*','185.146.3.237'] 
else:
    ALLOWED_HOSTS = ['185.146.3.237','shym-college.kz']



# Application definition

INSTALLED_APPS = [
    'modeltranslation',
'ckeditor_uploader',
    'ckeditor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'employeesapp',
    'newsapp',
    'sapp',
    'specializationapp',
    'page'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'silkwaycollege.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'silkwaycollege.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'college5',
            'USER': 'postgres',
            'PASSWORD': '123',
            'HOST': 'localhost',
            'PORT':''
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'college4',
            'USER': 'bbb',
            'PASSWORD': 'baguvix123F',
            'HOST': 'localhost',
            'PORT':''
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]
X_FRAME_OPTIONS = 'SAMEORIGIN'

gettext = lambda s: s
LANGUAGES = (
    ('ru',gettext('Russian')),
    ('en',gettext('English')),
    ('kk', gettext('Kazakhstan')),
)

CKEDITOR_UPLOAD_PATH = "uploads/"


CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"


CKEDITOR_CONFIGS = {

    'default': {

     'toolbar': 'None'

    },

}