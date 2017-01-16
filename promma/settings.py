# -*- coding: utf-8 -*-
"""
Django settings for promma project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e$2du3ewc=oo3x*h=qbh*zd9q##r0q&4mbfx4oo#h!7&@dqwu6'

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
    'us', # о нас
    'index', # главная страница
    'uroki', # все полные уроки
    'lp', # удар левый прямой
    'pp', # удар правый прямой
    'pb', # правый боковой
    'lb', # левый боковой
    'lo', # левый оперкот
    'po', # правый опперкот
    'bk', # бэкфист
    'yumor', # юмор
    'lk', # лоу кик
    'udsr', # прямой удар с разворота
    'fk', # фронт кик
    'hk', # хай кик
    'ak', # ап кик
    'borba', # борьба
    'backmount', # удушение с зади
    'mount', # позиция с верху
    'sidemount', # позиция с ,боку
    'compressor', # настройка компрессора для сжатия файлов картинок



)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'promma.urls'

WSGI_APPLICATION = 'promma.wsgi.application'


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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = r'D:/django_3_level/promma/static/'

#начало настроек медиа

MEDIA_ROOT = r'D:/django_3_level/promma/static/media/' # не забудьте указать свой домен
MEDIA_URL = '/static/media/'
#конец настроек медиа


TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)




#настройку устанавливали после установки bootsrap для его переноса в папку static
#знает где искать файлы сторонних билиотек и где их хранить
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'bootstrap/'),
    os.path.join(BASE_DIR, "foundation"),
)
#'bootstrap' это название нашей папки
# далее collectstatic


#поиск статистических файлов
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder", #настройка compressor Для сжатия картинок

)

#настройки соmpressor
'''
https://django-compressor.readthedocs.io/en/latest/quickstart/#installation
- в папке django добавили файл .htaccess
1)активировали виртуальное окружение и
pip install django_compressor
2)В settings.py к INSTALLED_APPS добавляется  ‘compressor’
3)STATICFILES_FINDERS
‘compressor.finders.CompressorFinder’
4)в {% load compress %} в base.html возле load static
5){% compress css %} <!-- начало сжатия сss -->{% endcompress %}
6) {% load compress %}<!--сжатие js файлов-->{% endcompress %}<!--конец сжатия js файлов-->
7) после установки библиотеки перезагружаем сервер
'''