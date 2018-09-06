from ambition_screening.models.subject_screening import SubjectScreening
from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_constants.constants import ABNORMAL
from edc_model_admin import (
    ModelAdminFormAutoNumberMixin, ModelAdminInstitutionMixin,
    audit_fieldset_tuple, audit_fields, ModelAdminNextUrlRedirectMixin,
    ModelAdminNextUrlRedirectError, ModelAdminReplaceLabelTextMixin)
from edc_consent.modeladmin_mixins import ModelAdminConsentMixin
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import ambition_subject_admin
from ..forms import SubjectConsentForm
from ..models import SubjectConsent, SubjectVisit


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormAutoNumberMixin,
                      ModelAdminRevisionMixin, ModelAdminReplaceLabelTextMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        redirect_url = super().redirect_url(
            request, obj, post_url_continue=post_url_continue)
        if request.GET.dict().get('next'):
            url_name = request.GET.dict().get('next').split(',')[0]
            attrs = request.GET.dict().get('next').split(',')[1:]
            options = {k: request.GET.dict().get(k)
                       for k in attrs if request.GET.dict().get(k)}
            options.update(subject_identifier=obj.subject_identifier)
            try:
                redirect_url = reverse(url_name, kwargs=options)
            except NoReverseMatch as e:
                raise ModelAdminNextUrlRedirectError(
                    f'{e}. Got url_name={url_name}, kwargs={options}.')
        return redirect_url


@admin.register(SubjectConsent, site=ambition_subject_admin)
class SubjectConsentAdmin(ModelAdminConsentMixin, ModelAdminMixin, SimpleHistoryAdmin,
                          admin.ModelAdmin):

    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'subject_identifier',
                'first_name',
                'last_name',
                'initials',
                'language',
                'is_literate',
                'witness_name',
                'consent_datetime',
                'dob',
                'guardian_name',
                'is_dob_estimated',
                'identity',
                'identity_type',
                'confirm_identity',
                'is_incarcerated')}),
        ('Sample collection and storage', {
            'fields': (
                'may_store_samples',
                'may_store_genetic_samples')}),
        ('Review Questions', {
            'fields': (
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_signature',
                'consent_copy'),
            'description': 'The following questions are directed to the interviewer.'}),
        audit_fieldset_tuple)

    search_fields = ('subject_identifier', 'screening_identifier', 'identity')

    radio_fields = {
        "assessment_score": admin.VERTICAL,
        "consent_copy": admin.VERTICAL,
        "consent_reviewed": admin.VERTICAL,
        "consent_signature": admin.VERTICAL,
        "gender": admin.VERTICAL,
        "is_dob_estimated": admin.VERTICAL,
        "identity_type": admin.VERTICAL,
        "is_incarcerated": admin.VERTICAL,
        "is_literate": admin.VERTICAL,
        "language": admin.VERTICAL,
        "may_store_genetic_samples": admin.VERTICAL,
        "may_store_samples": admin.VERTICAL,
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
        obj = SubjectConsent.objects.get(id=object_id)
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

    def get_form(self, request, obj=None, **kwargs):
        """Returns a form after replacing
        'participant' with 'next of kin'.
        """
        form = super().get_form(request, obj=obj, **kwargs)
        subject_screening = SubjectScreening.objects.get(
            screening_identifier=request.GET.get('screening_identifier'))
        if subject_screening.mental_status == ABNORMAL:
            form = self.replace_label_text(
                form, 'participant', 'next of kin', skip_fields=['is_incarcerated'])
        return form
