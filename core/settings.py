"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import dj_database_url
from pathlib import Path
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s7j71)53oc4+86p4_#5%v5+i)g-7zlqshu^r*2tm*wx=j&4m=a'

# SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

# DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
DEBUG = os.environ.get('DEBUG', 'True')=="True"

# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1',        
    'http://localhost',
    'https://deverdecasa.onrender.com'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    # 'api_rest',
    'dever',
    'login',
    'rolepermissions',
    

]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 
# DATABASES = {'default': dj_database_url.config(default='postgresql://deverdecasa_db_user:U3fHj0MjoE1AHGSuHizRIDMHDSsDkbwj@dpg-cskh7opu0jms73bc4r20-a.oregon-postgres.render.com/deverdecasa_db', conn_max_age=600)}

# DATABASES = {'default': dj_database_url.config(default='postgresql://deverdecasa_db_user:U3fHj0MjoE1AHGSuHizRIDMHDSsDkbwj@dpg-cskh7opu0jms73bc4r20-a/deverdecasa_db', conn_max_age=600)}
# DATABASES = {'default': dj_database_url.config(default='postgresql://postgres:postgres@localhost:5432/deverdecasa_db', conn_max_age=600)}
#postgresql://deverdecasa_db_user:U3fHj0MjoE1AHGSuHizRIDMHDSsDkbwj@dpg-cskh7opu0jms73bc4r20-a/deverdecasa_db

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'login.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório onde os arquivos estáticos serão coletados

if not DEBUG:  # Configuração para o ambiente de produção
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# URL para acessar arquivos estáticos no navegador


# Diretórios onde o Django buscará arquivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_ORIGINS = [
    'http://localhost:8080',
]

# settings.py
# LOGIN_URL = '/login/'

# Configuração para redirecionamento de login
LOGIN_URL = '/login/'  # Deve corresponder ao nome da sua URL de login
LOGIN_REDIRECT_URL = 'home'  # Página para redirecionar após login bem-sucedido
LOGOUT_REDIRECT_URL = 'home'  # Página para redirecionar após logout

# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ROLEPERMISSIONS_MODULE = 'login.roles'


# Configurações de Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # Ou seu servidor SMTP
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'seuemail@gmail.com'  # Substitua pelo seu email
# EMAIL_HOST_PASSWORD = 'suasenha'  # Substitua pela sua senha/app password
# DEFAULT_FROM_EMAIL = 'seuemail@gmail.com'  # Deve ser o mesmo que EMAIL_HOST_USER