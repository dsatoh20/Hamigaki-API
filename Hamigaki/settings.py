"""
Django settings for Hamigaki project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import json
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

try:
    with open('conf.json', 'r') as f:
        data = json.load(f)
    SECRET_KEY = data.get("SECRET_KEY", os.environ.get('SECRET_KEY'))
except FileNotFoundError:
    # conf.jsonがない場合はHerokuの環境変数から読み取る
    SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

allowed_hosts = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1')
ALLOWED_HOSTS = allowed_hosts.split(',')
# ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'hamigaki_app',
    'account'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Hamigaki.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Hamigaki.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


if 'JAWSDB_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            env='JAWSDB_URL',
            conn_max_age=600,

        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'hamigaki',
            'USER': 'root',
            'PASSWORD': data.get("DB_PASSWORD"),
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = "account.User" # accountアプリのUserモデルをデフォルトで使用する認証ユーザーモデルとして設定する

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


CORS_ALLOW_ALL_ORIGINS = False
cors_allowed_origins = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:3000")
# CORS_ALLOWED_ORIGINS = cors_allowed_origins.split(',')
CORS_ALLOWED_ORIGINS = ['*']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'Hamigaki.authentication.EmailBackend',
    'django.contrib.auth.backends.ModelBackend'
]

# CORS_ALLOW_ALL_ORIGINS = True  # すべてのオリジンを許可（本番環境では制限することが推奨）
CORS_ALLOW_CREDENTIALS = True  # クッキーを含むリクエストを許可

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # 静的ファイルを扱う

# RESTのAPIデフォルトのパーミッションクラス
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}

# csrf tokenについて

CSRF_COOKIE_SAMESITE = 'None'  # クロスオリジンでのクッキー共有を許可
CSRF_COOKIE_SECURE = True      # HTTPS通信が必須
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
# CSRF_USE_SESSIONS = True # cookieではなくsessionに保存
# CSRF_TRUSTED_ORIGINS = cors_allowed_origins.split(',')
CSRF_TRUSTED_ORIGINS = ['*']