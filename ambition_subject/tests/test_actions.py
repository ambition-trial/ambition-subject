from ambition_rando.import_randomization_list import import_randomization_list
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, tag
from edc_action_item.models.action_item import ActionItem
from edc_appointment.models.appointment import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy
from model_mommy.mommy import make_recipe
from pprint import pprint


class TestActions(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening')

        options = {
            'screening_identifier': subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        consent = mommy.make_recipe(
            'ambition_subject.subjectconsent', **options)

        self.subject_identifier = consent.subject_identifier

        self.appointment = Appointment.objects.get(
            subject_identifier=self.subject_identifier, visit_code='1000')
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=self.appointment,
            reason=SCHEDULED)

    @tag('9')
    def test_(self):
        obj = make_recipe(
            'ambition_subject.bloodresult',
            subject_visit=self.subject_visit,
            are_results_normal=NO,
            abnormal_results_in_ae_range=YES)

        try:
            ActionItem.objects.get(
                reference_identifier=obj.tracking_identifier)
        except ObjectDoesNotExist:
            self.fail('ActionItem unexpectedly does not exist.')

        try:
            obj = ActionItem.objects.get(
                parent_reference_identifier=obj.tracking_identifier)
        except ObjectDoesNotExist:
            self.fail('ActionItem unexpectedly does not exist.')

        pprint(obj.__dict__)