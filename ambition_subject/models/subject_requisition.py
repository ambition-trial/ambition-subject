# from django.db.models.deletion import PROTECT
from edc_lab.model_mixins import RequisitionModelMixin
from edc_model.models import BaseUuidModel
from edc_reference.model_mixins import ReferenceModelMixin

# from .subject_visit import SubjectVisit
# from edc_lab.managers import RequisitionManager as Manager


class SubjectRequisition(RequisitionModelMixin, ReferenceModelMixin, BaseUuidModel):

    #     subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    class Meta(RequisitionModelMixin.Meta):
        pass


# class SubjectRequisition(
#     NonUniqueSubjectIdentifierFieldMixin,
#     RequisitionModelMixin,
#     RequisitionStatusMixin,
#     RequisitionIdentifierMixin,
#     VisitTrackingCrfModelMixin,
#     SubjectScheduleCrfModelMixin,

#     RequiresConsentFieldsModelMixin,
#     PreviousVisitModelMixin,
#     RequisitionReferenceModelMixin,
#     UpdatesRequisitionMetadataModelMixin,
#     SearchSlugModelMixin,
#     BaseUuidModel,
# ):
#
#     subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)
#
#     reason_not_drawn = models.CharField(
#         verbose_name="If not drawn, please explain",
#         max_length=25,
#         default=NOT_APPLICABLE,
#         choices=REASON_NOT_DRAWN,
#     )
#
#     on_site = CurrentSiteManager()
#
#     objects = Manager()
#
#     history = HistoricalRecords()
#
#     def __str__(self):
#         return f"{self.requisition_identifier} " f"{self.panel_object.verbose_name}"
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             edc_protocol_app_config = django_apps.get_app_config(
#                 "edc_protocol")
#             self.protocol_number = edc_protocol_app_config.protocol_number
#         self.subject_identifier = self.subject_visit.subject_identifier
#         super().save(*args, **kwargs)
#
#     def get_search_slug_fields(self):
#         fields = super().get_search_slug_fields()
#         fields.extend(
#             ["requisition_identifier", "human_readable_identifier", "identifier_prefix"]
#         )
#         return fields
#
#     class Meta:
#         unique_together = ("panel", "subject_visit")
