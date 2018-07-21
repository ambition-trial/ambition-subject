from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_model_fields.fields import OtherCharField
from edc_visit_tracking.managers import CrfModelManager

from ..choices import FLUCONAZOLE_DOSE, YES_NO_ALREADY_ND
from ..managers import CurrentSiteManager
from .model_mixins import CrfModelMixin, ClinicalAssessmentModelMixin
from .model_mixins import SignificantDiagnosesModelMixin


class Week4DiagnosesManager(models.Manager):

    def get_by_natural_key(self, possible_diagnoses, dx_date, subject_identifier,
                           visit_schedule_name, schedule_name, visit_code):
        return self.get(
            possible_diagnoses=possible_diagnoses,
            dx_date=dx_date,
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code)


class Week4(ClinicalAssessmentModelMixin, CrfModelMixin):

    fluconazole_dose = models.CharField(
        verbose_name='Fluconazole dose (day prior to visit)',
        max_length=25,
        choices=FLUCONAZOLE_DOSE)

    fluconazole_dose_other = OtherCharField(
        max_length=25)

    rifampicin_started = models.CharField(
        verbose_name='Rifampicin started since last visit?',
        max_length=25,
        choices=YES_NO_ALREADY_ND)

    rifampicin_start_date = models.DateField(
        verbose_name='Date Rifampicin started',
        validators=[date_not_future],
        null=True,
        blank=True)

    lp_done = models.CharField(
        verbose_name='LP done?',
        max_length=5,
        choices=YES_NO,
        help_text='If yes, ensure LP CRF completed.')

    other_significant_dx = models.CharField(
        verbose_name='Other significant diagnosis since last visit?',
        max_length=5,
        choices=YES_NO_NA)

    on_site = CurrentSiteManager()

    objects = CrfModelManager()

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'Week 4'
        verbose_name_plural = 'Week 4'


class Week4Diagnoses(SignificantDiagnosesModelMixin, BaseUuidModel):

    week4 = models.ForeignKey(Week4, on_delete=PROTECT)

    objects = Week4DiagnosesManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.possible_diagnoses, self.dx_date) + self.week4.natural_key()
    natural_key.dependencies = ['ambition_subject.week4']

    class Meta:
        verbose_name = 'Week 4 Diagnoses'
        verbose_name_plural = 'Week 4 Diagnoses'
        unique_together = ('week4', 'possible_diagnoses', 'dx_date')
