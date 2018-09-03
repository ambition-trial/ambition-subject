from ambition_ae.action_items import AeInitialAction
from ambition_prn.action_items import StudyTerminationConclusionAction
from ambition_screening import EarlyWithdrawalEvaluator
from ambition_visit_schedule import DAY1
from edc_action_item import Action, site_action_items, HIGH_PRIORITY
from edc_constants.constants import YES

BLOOD_RESULTS_ACTION = 'abnormal-blood-result'
RECONSENT_ACTION = 'reconsent'


class BloodResultAction(Action):
    name = BLOOD_RESULTS_ACTION
    display_name = 'Reportable Blood Result'
    reference_model = 'ambition_subject.bloodresult'
    priority = HIGH_PRIORITY
    show_on_dashboard = True
    create_by_user = False

    def get_next_actions(self):
        actions = []
        self.delete_if_new(action_cls=AeInitialAction)
        if (self.reference_obj.subject_visit.visit_code == DAY1
                and self.reference_obj.subject_visit.visit_code_sequence == 0):
            # early withdrawal if qualifying blood results
            # are abnormal on DAY1.0
            evaluator = EarlyWithdrawalEvaluator(
                subject_identifier=self.reference_obj.subject_identifier)
            if not evaluator.eligible:
                actions = [StudyTerminationConclusionAction]
        elif (self.reference_obj.results_abnormal == YES
              and self.reference_obj.results_reportable == YES):
            # AE for reportable result, though not on DAY1.0
            actions = [AeInitialAction]
        return actions


class ReconsentAction(Action):
    name = RECONSENT_ACTION
    display_name = 'Re-consent participant'
    reference_model = 'ambition_subject.subjectreconsent'
    priority = HIGH_PRIORITY
    show_on_dashboard = True
    show_link_to_changelist = True
    admin_site_name = 'ambition_subject_admin'
    create_by_user = False
    singleton = True
    instructions = (
        'Participant must be re-consented as soon as able. '
        'Participant\'s ICF was initially completed by next-of-kin.')


site_action_items.register(BloodResultAction)
site_action_items.register(ReconsentAction)
