from django.conf import settings
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminAuditFieldsMixin,
    ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin,
    SimpleHistoryAdmin,
)
from edc_fieldsets import FieldsetsModelAdminMixin
from edc_notification import NotificationModelAdminMixin
from edc_sites.admin import ModelAdminSiteMixin
from edc_visit_tracking.modeladmin_mixins import CrfModelAdminMixin


class ModelAdminMixin(
    ModelAdminNextUrlRedirectMixin,
    NotificationModelAdminMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminRevisionMixin,
    ModelAdminAuditFieldsMixin,
    ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin,
    ModelAdminSiteMixin,
):

    list_per_page = 10
    date_hierarchy = "modified"
    empty_value_display = "-"


class CrfModelAdminMixin(CrfModelAdminMixin, ModelAdminMixin, FieldsetsModelAdminMixin):

    show_save_next = True
    show_cancel = True

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get("subject_dashboard_url")

    def post_url_on_delete_kwargs(self, request, obj):
        return dict(
            subject_identifier=obj.subject_visit.subject_identifier,
            appointment=str(obj.subject_visit.appointment.id),
        )

    def view_on_site(self, obj):
        dashboard_url_name = settings.DASHBOARD_URL_NAMES.get("subject_dashboard_url")
        try:
            url = reverse(
                dashboard_url_name,
                kwargs=dict(
                    subject_identifier=obj.subject_visit.subject_identifier,
                    appointment=str(obj.subject_visit.appointment.id),
                ),
            )
        except NoReverseMatch:
            url = super().view_on_site(obj)
        return url


class CrfModelAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    pass
