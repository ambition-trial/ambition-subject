
from edc_identifier.simple_identifier import SimpleIdentifier


class ScreeningIdentifier(SimpleIdentifier):

    random_string_length = 5
    identifier_type = 'screening_identifier'
    template = 'S{device_id}{random_string}'
    model = 'ambition_screening.identifierhistory'
