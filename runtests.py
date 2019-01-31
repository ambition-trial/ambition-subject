#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from os.path import abspath, dirname, join


class DisableMigrations:

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


base_dir = dirname(abspath(__file__))
app_name = 'ambition_subject'

installed_apps = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_crypto_fields.apps.AppConfig",
    "django_revision.apps.AppConfig",
    "django_collect_offline.apps.AppConfig",
    "django_collect_offline_files.apps.AppConfig",
    "rest_framework",
    "rest_framework.authtoken",
    "edc_action_item.apps.AppConfig",
    "edc_base.apps.AppConfig",
    "edc_prn.apps.AppConfig",
    "edc_reference.apps.AppConfig",
    "edc_metadata_rules.apps.AppConfig",
    "edc_model_admin.apps.AppConfig",
    "edc_notification.apps.AppConfig",
    "edc_consent.apps.AppConfig",
    "edc_offstudy.apps.AppConfig",
    "edc_timepoint.apps.AppConfig",
    "edc_device.apps.AppConfig",
    "edc_registration.apps.AppConfig",
    "edc_visit_schedule.apps.AppConfig",
    "edc_visit_tracking.apps.AppConfig",
    "ambition_auth.apps.AppConfig",
    "ambition_labs.apps.AppConfig",
    "ambition_lists.apps.AppConfig",
    "ambition_ae.apps.AppConfig",
    "ambition_prn.apps.AppConfig",
    "ambition_screening.apps.AppConfig",
    "ambition_reference.apps.AppConfig",
    "ambition_rando.apps.AppConfig",
    "ambition_metadata_rules.apps.AppConfig",
    "ambition_form_validators.apps.AppConfig",
    "ambition_visit_schedule.apps.AppConfig",
    "ambition_subject.apps.EdcFacilityAppConfig",
    "ambition_subject.apps.EdcLabAppConfig",
    "ambition_subject.apps.EdcMetadataAppConfig",
    "ambition_subject.apps.EdcIdentifierAppConfig",
    "ambition_subject.apps.EdcProtocolAppConfig",
    "ambition_subject.apps.EdcAppointmentAppConfig",
    "ambition_subject.apps.AppConfig",
]

DEFAULT_SETTINGS = dict(
    BASE_DIR=base_dir,
    ALLOWED_HOSTS=['localhost'],
    # AUTH_USER_MODEL='custom_user.CustomUser',
    ROOT_URLCONF=f'{app_name}.urls',
    STATIC_URL='/static/',
    INSTALLED_APPS=installed_apps,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        },
    },
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }],
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.contrib.sites.middleware.CurrentSiteMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "edc_dashboard.middleware.DashboardMiddleware",
        "edc_subject_dashboard.middleware.DashboardMiddleware",
    ],

    LANGUAGE_CODE='en-us',
    TIME_ZONE='UTC',
    USE_I18N=True,
    USE_L10N=True,
    USE_TZ=True,

    APP_NAME=app_name,
    COUNTRY="botswana",
    DEVICE_ID="99",
    DASHBOARD_URL_NAMES={
        "subject_listboard_url": "ambition_dashboard:subject_listboard_url",
        "screening_listboard_url": "ambition_dashboard:screening_listboard_url",
        "subject_dashboard_url": "ambition_dashboard:subject_dashboard_url",
    },
    DASHBOARD_BASE_TEMPLATES={
        "listboard_base_template": "ambition/base.html",
        "dashboard_base_template": "ambition/base.html",
        "screening_listboard_template": "ambition_dashboard/screening/listboard.html",
        "subject_listboard_template": "ambition_dashboard/subject/listboard.html",
        "subject_dashboard_template": "ambition_dashboard/subject/dashboard.html",
    },
    DJANGO_COLLECT_OFFLINE_FILES_REMOTE_HOST=None,
    DJANGO_COLLECT_OFFLINE_FILES_USB_VOLUME=None,
    DJANGO_COLLECT_OFFLINE_FILES_USER=None,
    DJANGO_COLLECT_OFFLINE_SERVER_IP=None,
    EDC_BOOTSTRAP=3,
    EMAIL_CONTACTS={
        "data_request": "someone@example.com",
        "data_manager": "someone@example.com",
        "tmg": "someone@example.com",
    },
    EMAIL_ENABLED=False,
    ETC_DIR=join(base_dir, "etc"),
    GIT_DIR=base_dir,
    HOLIDAY_FILE=join(base_dir, app_name, "tests", "holidays.csv"),
    LIVE_SYSTEM=False,
    SITE_ID=40,
    STATIC_ROOT=join(base_dir, app_name, "tests",
                     "ambition_subject", "static"),
    TWILIO_ACCOUNT_SID=None,
    TWILIO_AUTH_TOKEN=None,
    TWILIO_ENABLED=False,
    RANDOMIZATION_LIST_PATH=join(
        base_dir, app_name, "tests", "test_randomization_list.csv"),
    REVIEWER_SITE_ID=0,

    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    MIGRATION_MODULES=DisableMigrations(),
    PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher', ),
)

if os.environ.get("TRAVIS"):
    DEFAULT_SETTINGS.update(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'edc',
                'USER': 'travis',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '',
            },
        })


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    failures = DiscoverRunner(failfast=True).run_tests(
        [f'{app_name}.tests'])
    sys.exit(bool(failures))


if __name__ == "__main__":
    logging.basicConfig()
    main()
