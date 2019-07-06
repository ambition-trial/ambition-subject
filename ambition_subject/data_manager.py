from edc_data_manager .site_data_manager import site_data_manager
from edc_data_manager.rule import ModelHandler


class LumbarPunctureHandlerQ13(ModelHandler):

    name = "lumbar_puncture_q13"
    display_name = "Lumbar Puncture (Q13 ...)"
    model_name = "ambition_subject.lumbarpuncturecsf"

    @property
    def resolved(self):

        print(self.name)

        return True


site_data_manager.register(LumbarPunctureHandlerQ13)
