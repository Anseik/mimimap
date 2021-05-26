"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import my_settings
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = my_settings.SECRET_KEY

#이메일 인증관련 변수설정
EMAIL_BACKEND         = my_settings.EMAIL["EMAIL_BACKEND"]
EMAIL_USE_TLS         = my_settings.EMAIL["EMAIL_USE_TLS"]
EMAIL_PORT            = my_settings.EMAIL["EMAIL_PORT"]
EMAIL_HOST            = my_settings.EMAIL["EMAIL_HOST"]
EMAIL_HOST_USER       = my_settings.EMAIL["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD   = my_settings.EMAIL["EMAIL_HOST_PASSWORD"]
DEFAULT_FROM_EMAIL    = my_settings.EMAIL["DEFAULT_FROM_EMAIL"]
#SERVER_EMAIL          = my_settings.EMAIL["SERVER_EMAIL"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    my_settings.DOMAIN_URL,
    "127.0.0.1",
    "localhost"
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
    "api",
    "member",
    "recommendroad",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    

]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8081",
]

# 모든 경로 접속 허용 --> 차후 보안성 강화를 위해 제한해야한다.
CORS_ALLOW_ALL_ORIGINS = True

if DEBUG:
    MIDDLEWARE.append("backend.debug.DisableCSRF")

ROOT_URLCONF = "backend.urls"


CORS_ALLOWED_ORIGINS = [
    "https://j4d108.p.ssafy.io", 
    "http://j4d108.p.ssafy.io",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://192.168.0.4:8080"
]

CORS_ALLOW_METHODS  =  [ 
    'DELETE' , 
    'GET' , 
    'OPTIONS' , 
    'PATCH' , 
    'POST' , 
    'PUT' , 
]

CORS_ALLOW_HEADERS  =  [ 
    'accept' , 
    'accept-encoding' , 
    'authorization' , 
    'content-type' , 
    'dnt' , 
    'origin' , 
    'user-agent' , 
    'x-csrftoken' , 
    'x-requested-with' , 
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = my_settings.DATABASES

T_KEY = my_settings.T_KEY
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}

PASSWORD_HASHERS = (
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.SHA1PasswordHasher",
    "django.contrib.auth.hashers.MD5PasswordHasher",
    "django.contrib.auth.hashers.CryptPasswordHasher",
)

# MEDIA_URL = "/media/"

# MEDIA_ROOT = os.path.join(BASE_DIR, "media")