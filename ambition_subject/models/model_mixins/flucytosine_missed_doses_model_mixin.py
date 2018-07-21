from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_model_fields.fields import OtherCharField

from ...choices import REASON_DRUG_MISSED, DAYS_MISSED, DOSES_MISSED


class FlucytosineMissedDosesModelMixin(models.Model):

    flucy_day_missed = models.IntegerField(
        verbose_name='Day missed:',
        choices=DAYS_MISSED)

    flucy_doses_missed = models.IntegerField(
        verbose_name='Doses missed:',
        choices=DOSES_MISSED)

    flucy_missed_reason = models.CharField(
        verbose_name='Reason:',
        max_length=25,
        blank=True,
        choices=REASON_DRUG_MISSED)

    missed_reason_other = OtherCharField()

    history = HistoricalRecords()

    class Meta:
        abstract = True
