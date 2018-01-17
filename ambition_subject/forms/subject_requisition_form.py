from ambition_labs.panels import chemistry_panel, chemistry_alt_panel
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import YES, NO
from edc_lab.forms import RequisitionFormMixin
from edc_metadata.constants import NOT_REQUIRED

from ..models import SubjectRequisition
from .form_mixins import SubjectModelFormMixin


class SubjectRequisitionForm(SubjectModelFormMixin, RequisitionFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('reason_not_drawn') == NOT_REQUIRED:
            if self.cleaned_data.get('panel') == chemistry_panel.panel_model_obj:
                try:
                    self._meta.model.objects.get(
                        subject_visit=cleaned_data.get('subject_visit'),
                        panel=chemistry_alt_panel.panel_model_obj,
                        is_drawn=YES)
                except ObjectDoesNotExist:
                    raise forms.ValidationError(
                        {'reason_not_drawn': 'Invalid choice. At least one chemistry panel is expected.'})
            else:
                raise forms.ValidationError(
                    {'reason_not_drawn': 'Invalid choice. Not expected for this panel'})

        if (self.cleaned_data.get('panel') == chemistry_alt_panel.panel_model_obj
                and self.cleaned_data.get('is_drawn') == NO):
            try:
                self._meta.model.objects.get(
                    subject_visit=cleaned_data.get('subject_visit'),
                    panel=chemistry_panel.panel_model_obj,
                    reason_not_drawn=NOT_REQUIRED)
            except ObjectDoesNotExist:
                pass
            else:
                raise forms.ValidationError(
                    f'Remove the "{chemistry_panel.name}" requisition before '
                    f'setting this requisition to not drawn.')

        return cleaned_data

    class Meta:
        model = SubjectRequisition
        fields = '__all__'
