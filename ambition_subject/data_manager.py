from ambition_subject.constants import AWAITING_RESULTS
from edc_constants.constants import NOT_DONE, YES, NO
from edc_data_manager.rule import ModelHandler
from edc_data_manager.site_data_manager import site_data_manager


class LumbarPunctureHandlerQ13(ModelHandler):

    name = "lumbar_puncture_q13"
    display_name = "Lumbar Puncture (Q13, 15, 21, 23, 24)"
    model_name = "ambition_subject.lumbarpuncturecsf"

    @property
    def resolved(self):
        """Lumbar Puncture/Cerebrospinal Fluid 13, 15, 21, 23, 24.
        """
        resolved = False
        if self.get_field_value("csf_culture") == AWAITING_RESULTS:
            pass
        elif self.get_field_value("csf_culture") == NOT_DONE:
            resolved = True
        elif self.get_field_value("csf_culture") == YES:
            if (
                self.get_field_value("other_csf_culture")
                and self.get_field_value("csf_wbc_cell_count")
                and self.get_field_value("csf_glucose")
                and self.get_field_value("csf_protein")
                and (
                    self.get_field_value("csf_cr_ag")
                    or self.get_field_value("india_ink")
                )
            ):
                resolved = True
        elif self.get_field_value("csf_culture") == NO:
            if (
                self.get_field_value("csf_wbc_cell_count")
                and self.get_field_value("csf_glucose")
                and self.get_field_value("csf_protein")
                and (
                    self.get_field_value("csf_cr_ag")
                    or self.get_field_value("india_ink")
                )
            ):
                resolved = True
        return resolved


site_data_manager.register(LumbarPunctureHandlerQ13)
