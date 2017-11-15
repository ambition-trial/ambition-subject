from django.apps import apps as django_apps
from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_lab.model_mixins.requisition import RequisitionIdentifierMixin
from edc_lab.model_mixins.requisition import RequisitionModelMixin, RequisitionStatusMixin
from edc_metadata.model_mixins.updates import UpdatesRequisitionMetadataModelMixin
from edc_offstudy.model_mixins import OffstudyModelMixin
from edc_reference.model_mixins import RequisitionReferenceModelMixin
from edc_search.model_mixins import SearchSlugManager
from edc_visit_tracking.managers import CrfModelManager as VisitTrackingCrfModelManager
from edc_visit_tracking.model_mixins import CrfModelMixin as VisitTrackingCrfModelMixin
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin

from .model_mixins import SearchSlugModelMixin
from .subject_visit import SubjectVisit


class Manager(VisitTrackingCrfModelManager, SearchSlugManager):
    pass


class SubjectRequisition(
        RequisitionModelMixin, RequisitionStatusMixin, RequisitionIdentifierMixin,
        VisitTrackingCrfModelMixin, OffstudyModelMixin,
        RequiresConsentMixin, PreviousVisitModelMixin,
        RequisitionReferenceModelMixin, UpdatesRequisitionMetadataModelMixin,
        SearchSlugModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    objects = Manager()

    def save(self, *args, **kwargs):
        if not self.id:
            edc_protocol_app_config = django_apps.get_app_config(
                'edc_protocol')
            self.protocol_number = edc_protocol_app_config.protocol_number
            self.study_site = edc_protocol_app_config.site_code
            self.study_site_name = edc_protocol_app_config.site_name
        super().save(*args, **kwargs)

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend([
            'requisition_identifier',
            'human_readable_identifier', 'identifier_prefix'])
        return fields

    class Meta(VisitTrackingCrfModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
