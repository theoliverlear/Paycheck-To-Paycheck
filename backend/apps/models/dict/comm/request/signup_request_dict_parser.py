from injector import inject

from backend.apps.comm.request.signup_request import SignupRequest
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.dict_parser import DictParser


class SignupRequestDictParser(DictParser):
    @inject
    def __init__(self, class_dict_parser: ClassFieldParser[SignupRequest]):
        self.class_dict_parser: ClassFieldParser[SignupRequest] = class_dict_parser

    def get_signup_request(self, dict_data: dict):
        signup_request = {}
        for key in self.class_dict_parser.get_class_fields():
            signup_request[key] = self.parse(dict_data, key)
        return SignupRequest(**signup_request)