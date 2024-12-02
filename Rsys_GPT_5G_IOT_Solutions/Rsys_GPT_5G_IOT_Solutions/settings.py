"""
Django settings for Rsys_GPT_5G_IOT_Solutions project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)_tpzby)oj_qwkp*!tmkwr%ji*c5(12v_ia#r7-&wrpl-76#!v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["github.com/HarshatDy/RadisysOneToolNR","0.0.0.0","0.0.0.0"]


# Application definition

INSTALLED_APPS = [
    'All_Tools',
    'django_matplotlib',
    'Frequency_Tool_5G',
    'Global_Result_Tool_5G',
    'Link_Budget_Tool_5G',
    'NR_ARFCN_GSCN_Tool_5G',
    "whitenoise.runserver_nostatic",
    'ODU_CPU_Utilization_Tool_5G',
    'Du_Log_Parser_Tool_5G',
    'Power_Tool_5G',
    'RE_Mapping_Tool_5G',
    'Throughput_Tool_5G',
    'OTA_Algo_Tool_5G',
    'PTP_Timing_Delay_Parsing_Tool_5G',
    'Qual_Log_Parsing_Tool_5G',
    'NR_Cell_Identity_Tool_5G',
    'NR_TBS_Tool_5G',
    'NR_EPRE_Tool_5G',
    'NR_TA_Tool_5G',
    'NR_Free_Space_Path_Loss_Tool_5G',
    'NEC_ORU_FH_PICS_Tool_5G',
    'NEC_CUS_IOT_Profile_NR_TDD_Tool_5G',
    'NEC_ORAN_CUSPlane_SOC_8T8R_NEC_RU_Tool_5G',
    'RC23_6_Featurebitmap_Tool_5G',
    'RC23_6_FeatureSet_Tool_5G',
    'Sunwave_IOT_Parameter_Tool_5G',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Rsys_GPT_5G_IOT_Solutions.urls'

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

WSGI_APPLICATION = 'Rsys_GPT_5G_IOT_Solutions.wsgi.application'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
import os

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
