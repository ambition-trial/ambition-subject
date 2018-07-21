from django.contrib import admin
from edc_model_admin import TabularInlineMixin
from edc_model_admin import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import ambition_subject_admin
from ..forms import (Week2Form, AmphotericinMissedDosesForm,
                     FlucytosineMissedDosesForm, FluconazoleMissedDosesForm,
                     SignificantDiagnosesForm)
from .modeladmin_mixins import ModelAdminMixin
from ..models import (
    Week2, FluconazoleMissedDoses, AmphotericinMissedDoses,
    SignificantDiagnoses, FlucytosineMissedDoses)


class SignificantDiagnosesInline(TabularInlineMixin, admin.TabularInline):

    model = SignificantDiagnoses
    form = SignificantDiagnosesForm
    extra = 1

    fieldsets = (
        ['Admission history', {
            'fields': (
                'possible_diagnoses',
                'dx_date',
                'dx_other')},
         ],)


class AmphotericinMissedDosesInline(TabularInlineMixin, admin.TabularInline):

    model = AmphotericinMissedDoses
    form = AmphotericinMissedDosesForm
    extra = 1

    fieldsets = (
        ['Admission history', {
            'fields': (
                'ampho_day_missed',
                'ampho_missed_reason',
                'missed_reason_other')},
         ],)


class FluconazoleMissedDosesInline(TabularInlineMixin, admin.TabularInline):

    model = FluconazoleMissedDoses
    form = FluconazoleMissedDosesForm
    extra = 1

    fieldsets = (
        ['Admission history', {
            'fields': (
                'flucon_day_missed',
                'flucon_missed_reason',
                'missed_reason_other')},
         ],)


class FlucytosineMissedDosesInline(TabularInlineMixin, admin.TabularInline):

    model = FlucytosineMissedDoses
    form = FlucytosineMissedDosesForm
    extra = 1

    fieldsets = (
        ['Admission history', {
            'fields': (
                'flucy_day_missed',
                'flucy_doses_missed',
                'flucy_missed_reason',
                'missed_reason_other')},
         ],)


@admin.register(Week2, site=ambition_subject_admin)
class Week2Admin(ModelAdminMixin, SimpleHistoryAdmin, admin.ModelAdmin):

    form = Week2Form

    inlines = [SignificantDiagnosesInline, FluconazoleMissedDosesInline,
               AmphotericinMissedDosesInline, FlucytosineMissedDosesInline]

    fieldsets = (
        ['Admission history', {
            'fields': (
                'subject_visit',
                'report_datetime',
                'discharged',
                'discharge_date',
                'research_discharge_date',
                'died',
                'death_date_time')},
         ],
        ['Induction phase Study medication', {
            'fields': (
                'ampho_start_date',
                'ampho_end_date',
                'flucon_start_date',
                'flucon_stop_date',
                'flucy_start_date',
                'flucy_stop_date',
                'ambi_start_date',
                'ambi_stop_date',
                'drug_intervention',
                'drug_intervention_other',
                'antibiotic',
                'antibiotic_other',
                'blood_received',
                'units')}
         ],
        ['Clinical Assessment', {
            'fields': (
                'headache',
                'glasgow_coma_score',
                'confusion',
                'recent_seizure_less_72',
                'cn_palsy',
                'behaviour_change',
                'focal_neurology',
                'weight',
                'medicines',
                'medicine_other',
                'other_significant_dx'
            )}
         ],
        audit_fieldset_tuple
    )

    radio_fields = {
        'discharged': admin.VERTICAL,
        'died': admin.VERTICAL,
        'flucon_missed_doses': admin.VERTICAL,
        'amphotericin_missed_doses': admin.VERTICAL,
        'blood_received': admin.VERTICAL,
        'headache': admin.VERTICAL,
        'recent_seizure_less_72': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'cn_palsy': admin.VERTICAL,
        'focal_neurology': admin.VERTICAL,
        'other_significant_dx': admin.VERTICAL
    }
    filter_horizontal = ('antibiotic', 'medicines', 'drug_intervention')
