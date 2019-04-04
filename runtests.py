#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join


app_name = 'ambition_subject'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    EMAIL_CONTACTS={
        "data_request": "someone@example.com",
        "data_manager": "someone@example.com",
        "tmg": "someone@example.com",
    },
    EMAIL_ENABLED=True,
    HOLIDAY_FILE=join(base_dir, app_name, "tests", "holidays.csv"),
    LIVE_SYSTEM=False,
    RANDOMIZATION_LIST_PATH=join(
        base_dir, app_name, "tests", "test_randomization_list.csv"),
    INSTALLED_APPS=[
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
        "edc_dashboard.apps.AppConfig",
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
        "ambition_permissions.apps.AppConfig",
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
    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
).settings


#     DASHBOARD_BASE_TEMPLATES={
#         "listboard_base_template": "ambition/base.html",
#         "dashboard_base_template": "ambition/base.html",
#         "screening_listboard_template": "ambition_dashboard/screening/listboard.html",
#         "subject_listboard_template": "ambition_dashboard/subject/listboard.html",
#         "subject_dashboard_template": "ambition_dashboard/subject/dashboard.html",
#     },
#     STATIC_ROOT=join(base_dir, app_name, "tests",
#                      "ambition_subject", "static"),

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
