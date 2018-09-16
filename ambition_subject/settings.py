import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = 'ambition_subject'
ETC_DIR = os.path.join(BASE_DIR, 'etc')
SITE_ID = 40
REVIEWER_SITE_ID = 0

RANDOMIZATION_LIST_PATH = os.path.join(BASE_DIR, APP_NAME, 'tests',
                                       'test_randomization_list.csv')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jwggbn11gw22h6&0n@q0t97e)&)pg^n_*$18xj350f0%w+ywba'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'django_collect_offline.apps.AppConfig',
    'django_collect_offline_files.apps.AppConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'edc_action_item.apps.AppConfig',
    'edc_base.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_offstudy.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_visit_tracking.apps.AppConfig',
    'ambition_auth.apps.AppConfig',
    'ambition_labs.apps.AppConfig',
    'ambition_ae.apps.AppConfig',
    'ambition_prn.apps.AppConfig',
    'ambition_screening.apps.AppConfig',
    'ambition_reference.apps.AppConfig',
    'ambition_rando.apps.AppConfig',
    'ambition_metadata_rules.apps.AppConfig',
    'ambition_validators.apps.AppConfig',
    'ambition_visit_schedule.apps.AppConfig',
    'ambition_subject.apps.EdcFacilityAppConfig',
    'ambition_subject.apps.EdcLabAppConfig',
    'ambition_subject.apps.EdcMetadataAppConfig',
    'ambition_subject.apps.EdcIdentifierAppConfig',
    'ambition_subject.apps.EdcProtocolAppConfig',
    'ambition_subject.apps.EdcAppointmentAppConfig',
    'ambition_subject.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'ambition_subject.urls'

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

WSGI_APPLICATION = 'ambition_subject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('af', 'Afrikaans'),
    ('ny', 'Chichewa'),
    ('en', 'English'),
    ('xh', 'isiXhosa'),
    ('lg', 'Luganda'),
    ('rny', 'Runyankore'),
    ('tn', 'Setswana'),
    ('sn', 'Shona'))

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, APP_NAME, 'tests',
                           'ambition_subject', 'static')
STATIC_URL = '/static/'
DEVICE_ID = '99'

COUNTRY = 'botswana'
HOLIDAY_FILE = os.path.join(BASE_DIR, APP_NAME, 'tests', 'holidays.csv')
GIT_DIR = BASE_DIR

DJANGO_COLLECT_OFFLINE_SERVER_IP = None
DJANGO_COLLECT_OFFLINE_FILES_REMOTE_HOST = None
DJANGO_COLLECT_OFFLINE_FILES_USER = None
DJANGO_COLLECT_OFFLINE_FILES_USB_VOLUME = None

DASHBOARD_URL_NAMES = {
    'subject_listboard_url': 'ambition_dashboard:subject_listboard_url',
    'screening_listboard_url': 'ambition_dashboard:screening_listboard_url',
    'subject_dashboard_url': 'ambition_dashboard:subject_dashboard_url',
}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'ambition/base.html',
    'dashboard_base_template': 'ambition/base.html',
    'screening_listboard_template': 'ambition_dashboard/screening/listboard.html',
    'subject_listboard_template': 'ambition_dashboard/subject/listboard.html',
    'subject_dashboard_template': 'ambition_dashboard/subject/dashboard.html',
}

EDC_BOOTSTRAP = 3

if 'test' in sys.argv:

    class DisableMigrations:

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher', )
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
