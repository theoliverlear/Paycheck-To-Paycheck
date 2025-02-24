from injector import Provider

from backend.apps.models.dict.class_field_parser import ClassFieldParser


class ClassDictParserProvider(Provider):
    def __init__(self, target_class):
        self.target_class = target_class

    def get(self, injector):
        return ClassFieldParser(self.target_class)