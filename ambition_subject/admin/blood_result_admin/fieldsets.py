from edc_action_item import action_fieldset
from edc_fieldsets import Fieldset
from edc_model_admin import audit_fieldset_tuple

results_fieldsets = []
fields = [
    ('creatinine', 'RFT', None),
    ('urea', 'RFT', None),
    ('sodium', 'RFT', None),
    ('potassium', 'RFT', None),
    ('magnesium', 'RFT', None),
    ('alt', 'LFT', 'urea'),
    ('haemoglobin', 'CBC', None),
    ('wbc', 'CBC', None),
    ('neutrophil', 'CBC', None),
    ('platelets', 'CBC', None),
    ('cd4', 'Immunology', None),
    ('vl', 'Immunology', None),
]

for field, label, insert_after in fields:
    fieldset = Fieldset(
        field, f'{field}_units', f'{field}_abnormal', f'{field}_reportable',
        section=f'{label}: {field.upper()}')
    results_fieldsets.append(fieldset.fieldset)

biosynex_fieldset = Fieldset(
    'bios_crag',
    'crag_control_result',
    'crag_t1_result',
    'crag_t2_result',
    section='BIOSYNEX® CryptoPS (Semi-quantitative CrAg)')

fieldset = [(None, {'fields': ('subject_visit',)})]
fieldset.extend(results_fieldsets)
fieldset.append(('Conclusion', {
    'fields': ('results_abnormal', 'results_reportable')}))
fieldset.append(
    ('Summary', {'classes': ('collapse', ), 'fields': ('summary', )}))
fieldset.append(action_fieldset)
fieldset.append(audit_fieldset_tuple)
