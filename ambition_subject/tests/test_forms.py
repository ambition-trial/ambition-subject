import pytz

from ambition_labs.panels import wb_panel
from ambition_rando.tests import AmbitionTestCaseMixin
from ambition_visit_schedule.constants import DAY1
from datetime import datetime
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_constants.constants import YES, NO
from edc_lab.constants import TUBE
from edc_utils import get_utcnow
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy

from ..forms import SubjectRequisitionForm


class TestForms(AmbitionTestCaseMixin, TestCase):
    def setUp(self):
        year = get_utcnow().year
        subject_screening = mommy.make_recipe("ambition_screening.subjectscreening")
        consent = mommy.make_recipe(
            "ambition_subject.subjectconsent",
            screening_identifier=subject_screening.screening_identifier,
            consent_datetime=datetime(year, 12, 1, 0, 0, 0, 0, pytz.utc),
        )
        self.subject_identifier = consent.subject_identifier
        self.appointment = Appointment.objects.get(
            subject_identifier=self.subject_identifier, visit_code=DAY1
        )
        self.subject_visit = mommy.make_recipe(
            "ambition_subject.subjectvisit",
            appointment=self.appointment,
            reason=SCHEDULED,
        )

        self.data = {
            "clinic_verified": YES,
            "clinic_verified_datetime": get_utcnow(),
            "drawn_datetime": None,
            "item_type": TUBE,
            "panel": wb_panel,
            "reason_not_drawn": None,
            "report_datetime": get_utcnow(),
            "requisition_datetime": get_utcnow(),
            "requisition_identifier": None,
            "subject_identifier": self.subject_identifier,
            "subject_visit": self.subject_visit,
        }

    def test_(self):
        data = {"is_drawn": YES}
        form = SubjectRequisitionForm(data=data)
        form.is_valid()
        self.assertIn("drawn_datetime", form.errors.keys())
        self.assertEqual(["This field is required."], form.errors.get("drawn_datetime"))

        data = {"is_drawn": NO, "drawn_datetime": get_utcnow()}
        form = SubjectRequisitionForm(data=data)
        form.is_valid()
        self.assertIn("drawn_datetime", form.errors.keys())
        self.assertEqual(
            ["This field is not required."], form.errors.get("drawn_datetime")
        )
