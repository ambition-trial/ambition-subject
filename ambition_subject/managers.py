from django.contrib.sites.managers import CurrentSiteManager as BaseCurrentSiteManager
from edc_visit_tracking.managers import CrfModelManager


class CurrentSiteManager(BaseCurrentSiteManager, CrfModelManager):
    pass
