import pytz

from ambition_rando.tests import AmbitionTestCaseMixin
from ambition_visit_schedule.constants import WEEK10
from datetime import datetime
from django.apps import apps as django_apps
from django.contrib.auth.models import User, Permission
from django.contrib.sites.models import Site
from django.test import TestCase, tag
from django.test.client import RequestFactory
from django.test.utils import override_settings
from edc_appointment.models.appointment import Appointment
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy

from ..admin_site import ambition_subject_admin
from ..models import FollowUp, SubjectVisit
from ambition_sites.sites import fqdn, ambition_sites
from edc_base.sites.utils import add_or_update_django_sites


@override_settings(SITE_ID='10')
class TestFollowUp(AmbitionTestCaseMixin, TestCase):

    def setUp(self):
        add_or_update_django_sites(
            apps=django_apps, sites=ambition_sites, fqdn=fqdn, verbose=False)
        self.user = User.objects.create(
            username='erikvw',
            is_staff=True,
            is_active=True)
        for permission in Permission.objects.filter(
                content_type__app_label='ambition_subject',
                content_type__model='followup'):
            self.user.user_permissions.add(permission)

        subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening')
        consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            screening_identifier=subject_screening.screening_identifier,
            consent_datetime=datetime(2017, 12, 1, 0, 0, 0, 0, pytz.utc))
        self.subject_identifier = consent.subject_identifier

        for appointment in Appointment.objects.filter(
                subject_identifier=self.subject_identifier).order_by('timepoint'):
            if appointment.visit_code == WEEK10:
                self.appointment = appointment
                self.subject_visit = SubjectVisit.objects.create(
                    appointment=appointment,
                    subject_identifier=self.subject_identifier,
                    reason=SCHEDULED)
                break
            else:
                SubjectVisit.objects.create(
                    appointment=appointment,
                    subject_identifier=self.subject_identifier,
                    reason=SCHEDULED)

    @tag('1')
    def test_(self):
        """Asserts custom antibiotic question shows for Week 10.
        """
        for model, model_admin in ambition_subject_admin._registry.items():
            if model == FollowUp:
                my_model_admin = model_admin.admin_site._registry.get(FollowUp)

        rf = RequestFactory()

        request = rf.get(f'/?appointment={str(self.appointment.id)}')

        request.user = self.user
        request.site = Site.objects.get_current()

        rendered_change_form = my_model_admin.changeform_view(
            request, None, '', {
                'subject_visit': self.subject_visit})
#         self.assertNotIn(
#             'Were any of the following antibiotics given?',
#             rendered_change_form.rendered_content)
        self.assertIn(
            'Were any of the following antibiotics given since week two?',
            rendered_change_form.rendered_content)
