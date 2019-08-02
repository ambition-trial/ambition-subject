from ambition_subject.models.patient_history import PatientHistory


def get_weight_for_timepoint(subject_identifier=None, reference_dt=None):
    qs = PatientHistory.objects.filter(
        subject_visit__appointment__subject_identifier=subject_identifier,
        report_datetime__lte=reference_dt,
    ).order_by("-report_datetime")
    if qs:
        return qs[0].weight
    return None
