from pathlib import Path
import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.core.cache import cache


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Projectizer.settings")

# # Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2+h7il=nd@75ys(rgiuw_9@fh78ngrzc*ip)^gfr14d7okvqav'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ALLOWED_HOSTS = ['*']
settings.DATA_UPLOAD_MAX_MEMORY_SIZE = 9242880
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myshop.apps.MyshopConfig',
    'users.apps.UsersConfig',
    'fontawesome_5',
    'silk',
    'taggit',
    'sorl.thumbnail',
    'parler',
    'rosetta', 
    'rest_framework',
    'django_celery_results',


]

from django.utils.translation import gettext_lazy as _
LANGUAGES=(
    ('uz',_("Uzbek")),
    ('en',_("English")),
)

FONTAWESOME_5_CSS = 'static/css/fontawesome.min.css' 
FONTAWESOME_PREFIX ='fa'
SILKY_MIDDLEWARE_CLASS = 'path.to.your.middleware.MyCustomSilkyMiddleware'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'silk.middleware.SilkyMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'projectshop.urls'
TEMPLATE_DIR=os.path.join(BASE_DIR,"template")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'myshop.cart_context.cart_context',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'projectshop.wsgi.application'
CELERY_RESULT_BACKEND = 'django-db'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

PARLER_LANGUAGES={
    None:(
        {'code':'en'},
        {'code':'uz'},
    ),
    'default':{
        'fallbacks':['en'],
        'hide_untranslated':False
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/' # URL для медии в шаблонах


STATIC_ROOT = os.path.join(BASE_DIR, 'static') # пустая папка, сюда будет собирать статику collectstatic

STATIC_URL = '/static/' # URL для шаблонов


STATICFILES_DIRS = (

os.path.join(BASE_DIR, 'staticfiles'),

)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='ilhomjumayev6022@gmail.com'
EMAIL_HOST_PASSWORD='erkin2001041'

SESSIONS_ENGINE='django.contrib.sessions.backends.cache'

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }