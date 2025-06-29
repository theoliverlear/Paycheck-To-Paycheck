from injector import inject

from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.dict_parser import DictParser
from backend.apps.models.welcome.welcome_survey import WelcomeSurvey


class WelcomeSurveyDictParser(DictParser):
    @inject
    def __init__(self,
                 class_dict_parser: ClassFieldParser[WelcomeSurvey]):
        self.class_dict_parser: ClassFieldParser[WelcomeSurvey] = class_dict_parser

    def get_welcome_survey(self, dict_data: dict) -> WelcomeSurvey:
        for key in self.class_dict_parser.get_class_fields():
            dict_data[key] = self.parse(dict_data, key)
        return WelcomeSurvey(**dict_data)