from datetime import date

from injector import inject

from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.time.due_date import DueDate
from backend.apps.models.date_utilities import iso_to_django_date
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.dict_parser import DictParser


class OneTimeBillDictParser(DictParser):
    @inject
    def __init__(self, class_dict_parser: ClassFieldParser[OneTimeBill]):
        self.class_dict_parser = class_dict_parser

    def get_bill(self, dict_data):
        bill = {}
        for key in self.class_dict_parser.get_class_fields():
            print(f'Key: {key}')
            bill[key] = self.parse(dict_data, key)
            if isinstance(bill[key], date):
                bill[key] = DueDate(due_date=bill[key])
        return OneTimeBill(**bill)
