from edc_base.model_managers import HistoricalRecords
from edc_visit_tracking.managers import CrfModelManager

from ..managers import CurrentSiteManager
from .model_mixins import CrfModelMixin, EducationModelMixin


class EducationHoh(EducationModelMixin, CrfModelMixin):

    on_site = CurrentSiteManager()

    objects = CrfModelManager()

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = ('Health Economics: Education (Person who '
                        'earns the highest income)')
        verbose_name_plural = ('Health Economics: Education (Person '
                               'who earns the highest income)')
