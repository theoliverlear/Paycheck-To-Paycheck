from datetime import date

from injector import inject

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.time.due_date import DueDate
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.dict_parser import DictParser


class OneTimeBillDictParser(DictParser):
    @inject
    def __init__(self, class_dict_parser: ClassFieldParser[OneTimeBill]):
        self.class_dict_parser: ClassFieldParser[OneTimeBill] = class_dict_parser

    def add_normalized_date_key(self, dict_data: dict, check_date_received: bool = False):
        super().add_normalized_date_key(dict_data, False)

    def get_one_time_bill(self, dict_data: dict) -> OneTimeBill:
        keys_to_skip: list[str] = ['id', 'bill_history']
        bill: dict = {}
        for key in self.class_dict_parser.get_class_fields():
            if key not in keys_to_skip:
                bill[key] = self.parse(dict_data, key)
                if isinstance(bill[key], date):
                    bill[key] = DueDate(due_date=bill[key])
        one_time_bill: OneTimeBill = OneTimeBill(**bill)
        one_time_bill.bill_history = BillHistory()
        return one_time_bill
