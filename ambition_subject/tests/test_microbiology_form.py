from django.test import TestCase, tag
from model_mommy import mommy
from dateutil.relativedelta import relativedelta

from edc_base.utils import get_utcnow
from edc_constants.constants import NO, NOT_APPLICABLE, OTHER, POS, YES
from edc_visit_tracking.constants import SCHEDULED

from ..constants import HISTOPATHOLOGY_REPORT, VIBRIO
from ..forms import MicrobiologyForm
from ..models import Appointment, Microbiology


class TestMicrobiology(TestCase):

#     def setUp(self):
#         screening = mommy.make_recipe('ambition_subject.subject_screening',
# #                                       report_datetime=get_utcnow(),
#                                       )
#         consent = mommy.make_recipe(
#             'ambition_subject.subject_consent',
#             consent_datetime=get_utcnow(),
#             report_datetime=(get_utcnow() - relativedelta(years=1)).date(),
#             subject_screening=screening)
#         appointment = Appointment.objects.get(
#             visit_code='1000')
#         self.subject_visit = mommy.make_recipe(
#             'ambition_subject.subjectvisit',
#             appointment=appointment,
#             subject_identifier=consent.subject_identifier, reason=SCHEDULED,)

    @tag('micro')
    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,)
#                                    self.subject_visit.id)
#         obj.subject_visit = self.subject_visit
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    @tag('micro')
    def test_urine_culture_no_results_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results=NOT_APPLICABLE)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results='no_growth')
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_urine_culture_no_organism_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results=POS,
                                   urine_culture_organism=None)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results=POS,
                                   urine_culture_organism='e.coli')
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_urine_culture_not_performed_valid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=NO,
                                   urine_culture_results=NOT_APPLICABLE,
                                   urine_culture_organism=NOT_APPLICABLE,
                                   urine_culture_organism_other=None)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_blood_culture_no_results_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=NOT_APPLICABLE)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results='no_growth')
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_blood_culture_no_study_day_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=POS,
                                   blood_culture_organism='e.coli',
                                   day_blood_taken=NOT_APPLICABLE,)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=POS,
                                   blood_culture_organism='e.coli',
                                   day_blood_taken=9,)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_blood_culture_no_organism_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=POS,
                                   day_blood_taken=30,
                                   blood_culture_organism=NOT_APPLICABLE,)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=POS,
                                   day_blood_taken=5,
                                   blood_culture_organism='e.coli',)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_blood_culture_no_organism_other_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_organism=OTHER,
                                   blood_culture_organism_other=None)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_organism=OTHER,
                                   blood_culture_organism_other='blahblah')
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    @tag('micro')
    def test_tissue_biopsy_no_results_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=None)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results='no_growth',)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_tissue_biopsy_no_organism_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   day_biopsy_taken=5,
                                   tissue_biopsy_organism=None)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   day_biopsy_taken=7,
                                   tissue_biopsy_organism='cryptococcus_neoformans')
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_tissue_biopsy_no_organism_other_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   tissue_biopsy_organism=OTHER,
                                   day_biopsy_taken=12,
                                   tissue_biopsy_organism_other=None)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   day_biopsy_taken=7,
                                   tissue_biopsy_organism=OTHER,
                                   tissue_biopsy_organism_other='blahblah')
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_biopsy_culture_no_study_day_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   tissue_biopsy_organism='cryptococcus_neoformans',
                                   day_biopsy_taken=None)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   tissue_biopsy_organism='cryptococcus_neoformans',
                                   day_biopsy_taken=4)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('micro')
    def test_pos_sputum_no_results_invalid(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   sputum_results_culture=POS,
                                   sputum_results_positive=None,)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   sputum_results_culture=POS,
                                   sputum_results_positive='blahblah',)
        form = MicrobiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
