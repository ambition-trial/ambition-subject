from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from edc_model_admin import audit_fieldset_tuple, audit_fields
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import ambition_subject_admin
from ..forms import SubjectReconsentForm
from ..models import SubjectReconsent, SubjectVisit
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectReconsent, site=ambition_subject_admin)
class SubjectReconsentAdmin(ModelAdminMixin, SimpleHistoryAdmin, admin.ModelAdmin):

    form = SubjectReconsentForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'identity')}),
        ('Review Questions', {
            'fields': (
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_signature',
                'consent_copy'),
            'description': 'The following questions are directed to the interviewer.'}),
        audit_fieldset_tuple)

    search_fields = ('subject_identifier', 'identity')

    radio_fields = {
        "assessment_score": admin.VERTICAL,
        "consent_copy": admin.VERTICAL,
        "consent_reviewed": admin.VERTICAL,
        "consent_signature": admin.VERTICAL,
        "study_questions": admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)

    def view_on_site(self, obj):
        dashboard_url_name = settings.DASHBOARD_URL_NAMES.get(
            'subject_dashboard_url')
        try:
            return reverse(
                dashboard_url_name, kwargs=dict(
                    subject_identifier=obj.subject_identifier))
        except NoReverseMatch:
            return super().view_on_site(obj)

    def delete_view(self, request, object_id, extra_context=None):
        """Prevent deletion if SubjectVisit objects exist.
        """
        extra_context = extra_context or {}
        obj = SubjectReconsent.objects.get(id=object_id)
        try:
            protected = [SubjectVisit.objects.get(
                subject_identifier=obj.subject_identifier)]
        except ObjectDoesNotExist:
            protected = None
        except MultipleObjectsReturned:
            protected = SubjectVisit.objects.filter(
                subject_identifier=obj.subject_identifier)
        extra_context.update({'protected': protected})
        return super().delete_view(request, object_id, extra_context)
