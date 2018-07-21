from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin

from ..admin_site import ambition_subject_admin
from ..forms import PatientHistoryForm, PreviousOpportunisticInfectionForm
from ..models import PatientHistory, PreviousOpportunisticInfection
from .modeladmin_mixins import CrfModelAdminMixin


class PreviousOpportunisticInfectionInline(TabularInlineMixin, admin.TabularInline):

    model = PreviousOpportunisticInfection
    form = PreviousOpportunisticInfectionForm
    extra = 1

    fieldsets = (
        ['Previous Opportunistic Infection', {
            'fields': (
                'previous_non_tb_oi',
                'previous_non_tb_oi_other',
                'previous_non_tb_oi_date')},
         ],)


@admin.register(PatientHistory, site=ambition_subject_admin)
class PatientHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = PatientHistoryForm

    inlines = [PreviousOpportunisticInfectionInline]

    filter_horizontal = ('neurological', 'symptom', 'specify_medications')

    fieldsets = (
        ('Current Symptoms', {
            'fields': [
                'subject_visit',
                'report_datetime',
                'symptom',
                'headache_duration',
                'visual_loss_duration']}
         ),
        ('Previous Medical History', {
            'fields': [
                'tb_history',
                'tb_site',
                'tb_treatment',
                'taking_rifampicin',
                'rifampicin_started_date', ]}
         ),
        ('Previous Opportunistic Infections', {
            'fields': [
                'new_hiv_diagnosis',
                'taking_arv',
                'arv_date',
                'arv_date_estimated',
                'first_arv_regimen',
                'first_arv_regimen_other',
                'first_line_choice',
                'second_arv_regimen',
                'second_arv_regimen_other',
                'patient_adherence',
                'tablets_missed',
                'last_dose',
                'last_viral_load',
                'viral_load_date',
                'vl_date_estimated',
                'last_cd4',
                'cd4_date',
                'cd4_date_estimated']}
         ),
        ('Vital Signs', {
            'fields': [
                'temp',
                'heart_rate',
                'sys_blood_pressure',
                'dia_blood_pressure',
                'respiratory_rate',
                'weight',
                'weight_determination',
                'glasgow_coma_score']}
         ),
        ('Neurological', {
            'fields': [
                'neurological',
                'neurological_other',
                'focal_neurologic_deficit',
                'visual_acuity_day',
                'left_acuity',
                'right_acuity',
                'ecog_score']}
         ),
        ('Other', {
            'fields': [
                'lung_exam',
                'cryptococcal_lesions',
                'specify_medications',
                'specify_medications_other']}
         ),
        ('Previous Infection', {
            'fields': [
                'previous_oi']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'cd4_date_estimated': admin.VERTICAL,
        'cryptococcal_lesions': admin.VERTICAL,
        'ecog_score': admin.VERTICAL,
        'first_arv_regimen': admin.VERTICAL,
        'first_line_choice': admin.VERTICAL,
        'lung_exam': admin.VERTICAL,
        'tb_history': admin.VERTICAL,
        'new_hiv_diagnosis': admin.VERTICAL,
        'patient_adherence': admin.VERTICAL,
        'second_arv_regimen': admin.VERTICAL,
        'taking_arv': admin.VERTICAL,
        'arv_date_estimated': admin.VERTICAL,
        'taking_rifampicin': admin.VERTICAL,
        'tb_site': admin.VERTICAL,
        'tb_treatment': admin.VERTICAL,
        'vl_date_estimated': admin.VERTICAL,
        'previous_oi': admin.VERTICAL,
        'weight_determination': admin.VERTICAL}
