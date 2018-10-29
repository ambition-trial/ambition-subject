from ambition_form_validators import EducationFormValidator

from ..models import EducationHoh
from .form_mixins import SubjectModelFormMixin


class EducationHohForm(SubjectModelFormMixin):

    form_validator_cls = EducationFormValidator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profession'].label = ('What is their profession?')
        self.fields['education_years'].label = (
            'How many years of education did they complete?')
        self.fields['education_certificate'].label = (
            'What is the their highest education certificate?')
        self.fields['elementary'].label = (
            'Did they go to elementary/primary school?')
        self.fields['secondary'].label = (
            'Did they go to secondary school?')
        self.fields['higher_education'].label = (
            'Did they go to higher education?')

    class Meta:
        model = EducationHoh
        fields = '__all__'
