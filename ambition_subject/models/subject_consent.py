from django.apps import apps as django_apps
from django.db import models
from django.core.validators import RegexValidator
from django_crypto_fields.fields import (
    FirstnameField, LastnameField, EncryptedCharField)
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.field_mixins import SampleCollectionFieldsMixin, CitizenFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.field_mixins.bw import IdentityFieldsMixin
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_consent.validators import eligible_if_yes, eligible_if_yes_or_declined
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_search.model_mixins import SearchSlugManager


from ..choices import ID_TYPE, YES_NO_DECLINED
from .model_mixins import SearchSlugModelMixin
from .subject_screening import SubjectScreening


class SubjectConsentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class SubjectConsent(
        ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin,
        NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin,
        ReviewFieldsMixin, PersonalFieldsMixin,
        SampleCollectionFieldsMixin, CitizenFieldsMixin,
        VulnerabilityFieldsMixin, SearchSlugModelMixin, BaseUuidModel):
    """ A model completed by the user that captures the ICF.
    """

    first_name = FirstnameField(
        blank=False)

    last_name = LastnameField(
        verbose_name="Last name",
        blank=False
    )

    initials = EncryptedCharField(
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}$',
            message=('Ensure initials consist of letters '
                     'only in upper case, no spaces.')), ],
        blank=False
    )

    screening_identifier = models.CharField(
        verbose_name='Screening Identifier',
        max_length=50)

    is_signed = models.BooleanField(default=False, editable=False)

    may_store_genetic_samples = models.CharField(
        verbose_name=('Does the participant/next of kin agree that a portion of'
                      ' the blood sample that is taken be stored for genetic'
                      ' analysis?'),
        max_length=25,
        choices=YES_NO)

    identity_type = models.CharField(
        verbose_name='What type of identity number is this?',
        max_length=25,
        choices=ID_TYPE)

    may_store_samples = models.CharField(
        verbose_name=(
            'Does the participant/next of kin agree to have samples '
            'stored after the study has ended'),
        max_length=3,
        choices=YES_NO,
    )

    consent_reviewed = models.CharField(
        verbose_name='I have reviewed the consent with the participant',
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        null=True,
        blank=False,
        help_text='If no, INELIGIBLE',
    )
    study_questions = models.CharField(
        verbose_name=(
            'I have answered all questions the participant had about the study'),
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        null=True,
        blank=False,
        help_text='If no, INELIGIBLE',
    )
    assessment_score = models.CharField(
        verbose_name=(
            'I have asked the participant questions about this study and '
            'they have demonstrated understanding'),
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        null=True,
        blank=False,
        help_text='If no, INELIGIBLE',
    )

    consent_signature = models.CharField(
        verbose_name=('The participant has signed the consent form?'),
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        null=True,
        blank=False,
        help_text='If no, INELIGIBLE',
    )

    consent_copy = models.CharField(
        verbose_name=(
            'I have provided the participant with a copy of their '
            'signed informed consent'),
        max_length=20,
        choices=YES_NO_DECLINED,
        validators=[eligible_if_yes_or_declined, ],
        null=True,
        blank=False,
        help_text='If declined, return copy to the clinic with the consent',
    )
    objects = SubjectConsentManager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        subject_screening = SubjectScreening.objects.get(
            screening_identifier=self.screening_identifier)
        self.gender = subject_screening.gender
        if not self.id:
            self.registration_identifier = self.screening_identifier
            edc_protocol_app_config = django_apps.get_app_config(
                'edc_protocol')
            self.study_site = edc_protocol_app_config.site_code
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version,)

    @property
    def registration_unique_field(self):
        return 'subject_identifier'

    class Meta(ConsentModelMixin.Meta):
        get_latest_by = 'consent_datetime'
        unique_together = (('subject_identifier', 'version'),
                           ('subject_identifier', 'screening_identifier'),
                           ('first_name', 'dob', 'initials', 'version'))
        ordering = ('-created',)
