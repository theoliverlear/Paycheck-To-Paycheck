from injector import inject

from backend.apps.comm.request.login_request import LoginRequest
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.dict_parser import DictParser


class LoginRequestDictParser(DictParser):
    @inject
    def __init__(self, class_dict_parser: ClassFieldParser[LoginRequest]):
        self.class_dict_parser: ClassFieldParser[LoginRequest] = class_dict_parser

    def get_login_request(self, dict_data: dict):
        login_request = {}
        for key in self.class_dict_parser.get_class_fields():
            login_request[key] = self.parse(dict_data, key)
        return LoginRequest(**login_request)