from edc_reference.reference_model_config import ReferenceModelConfig
from edc_reference.site import site_reference_fields

reference = ReferenceModelConfig(
    model='ambition_subject.adverseevent',
    fields=['ae_severity_grade'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.prnmodel',
    fields=['adverse_event', 'adverse_event_tmg', 'adverse_event_followup',
            'microbiology', 'radiology', 'protocol_deviation', 'blood_result',
            'lumbar_puncture', 'recurrence_symptom', 'death_report'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.clinicnote',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.adverseeventfollowup',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.adverseeventtmg',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.bloodresult',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.deathreport',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.followup',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.patienthistory',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.protocoldeviationviolation',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.microbiology',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.radiology',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.lumbarpuncturecsf',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.recurrencesymptom',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.subjectrequisition',
    fields=['requisition_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.week2',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.week4',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.week16',
    fields=['report_datetime'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='ambition_subject.studyterminationconclusion',
    fields=['report_datetime', 'termination_reason'])
site_reference_fields.register(reference)
