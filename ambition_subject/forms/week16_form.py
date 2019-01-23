from ambition_form_validators import Week16FormValidator

from ..models import Week16
from .form_mixins import SubjectModelFormMixin


class Week16Form(SubjectModelFormMixin):

    form_validator_cls = Week16FormValidator

    class Meta:
        model = Week16
        fields = "__all__"
