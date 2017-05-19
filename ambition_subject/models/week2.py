from django.core.validators import MinValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO

from ..choices import (REASON_DRUG_MISSED, MEDICINES, DAYS_MISSED)
from .list_models import Antibiotic, OtherDrug
from .model_mixins import CrfModelMixin


class Week2(CrfModelMixin):

    discharged = models.CharField(
        verbose_name='Discharged?',
        max_length=25,
        choices=YES_NO)

    discharge_date = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    died = models.CharField(
        verbose_name='Died?',
        max_length=25,
        choices=YES_NO)

    death_date = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    flucon_start_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=True)

    flucon_stop_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=True)

    other_drug = models.ManyToManyField(
        OtherDrug,
        verbose_name="Other drugs/interventions given during first 14 days",)

    antibiotic = models.ManyToManyField(
        Antibiotic,
        verbose_name="if antibiotics, select the ones given",)

    blood_received = models.CharField(
        verbose_name='Blood transfusion received?',
        max_length=25,
        choices=YES_NO)

    units = models.IntegerField(
        verbose_name='If yes, No. of units',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    headache = models.CharField(
        verbose_name='Headache',
        max_length=25,
        choices=YES_NO,
        help_text="Confirm with patient")

    temperature = models.FloatField(
        verbose_name='Temperature',
        null=True,
        blank=True,
        default=None)

    glasgow_cs = models.IntegerField(
        verbose_name='Glasgow Coma Score',
        null=True,
        blank=True)

    seizures_during_admission = models.CharField(
        verbose_name='Seizures during admission',
        max_length=25,
        choices=YES_NO)

    recent_seizure = models.CharField(
        verbose_name='Recent seizure (<72 hrs):',
        max_length=25,
        choices=YES_NO)

    behaviour_change = models.CharField(
        verbose_name='Behaviour change',
        max_length=25,
        choices=YES_NO)

    confusion = models.CharField(
        verbose_name='Confusion',
        max_length=25,
        choices=YES_NO)

    cn_palsy = models.CharField(
        verbose_name='CN palsy',
        max_length=25,
        choices=YES_NO)

    focal_neurology = models.CharField(
        verbose_name='Focal Neurology:',
        max_length=25,
        choices=YES_NO)

    weight = models.IntegerField(
        null=True,
        blank=True,
        help_text='Weight in Kilograms')

    medicines = models.CharField(
        verbose_name='Medicines on Day 14:',
        max_length=25,
        choices=MEDICINES)

    significant_diagnosis = models.CharField(
        verbose_name='Other significant diagnoses since enrolment?',
        max_length=25,
        choices=YES_NO)

    flucon_missed_doses = models.CharField(
        verbose_name='Were any Fluconazole drug doses missed?',
        max_length=25,
        choices=YES_NO)

    amphotericin_missed_doses = models.CharField(
        verbose_name='Were any Amphotericin b drug doses missed?',
        max_length=25,
        choices=YES_NO)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'


class FluconazoleMissedDoses(BaseUuidModel):

    week2 = models.ForeignKey(Week2)

    day_missed = models.IntegerField(
        verbose_name='Day missed:',
        choices=DAYS_MISSED
    )

    flucon_missed_reason = models.CharField(
        verbose_name='Reason:',
        max_length=25,
        blank=True,
        choices=REASON_DRUG_MISSED)

    flucon_missed_reason_other = OtherCharField()

    class Meta:
        app_label = 'ambition_subject'
        unique_together = ('day_missed', 'flucon_missed_reason')


class AmphotericinMissedDoses(BaseUuidModel):

    week2 = models.ForeignKey(Week2)

    day_missed = models.IntegerField(
        verbose_name='Day:',
        choices=DAYS_MISSED
    )

    ampho_missed_reason = models.CharField(
        verbose_name='Were any drug doses missed?',
        max_length=25,
        choices=REASON_DRUG_MISSED)

    ampho_missed_reason_other = OtherCharField()

    class Meta:
        app_label = 'ambition_subject'
        unique_together = ('day_missed', 'ampho_missed_reason')
