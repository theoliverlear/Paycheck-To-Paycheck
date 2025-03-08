from injector import inject

from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.dict_parser import DictParser


class OneTimeIncomeDictParser(DictParser):
    @inject
    def __init__(self, class_dict_parser: ClassFieldParser[OneTimeIncome]):
        self.class_dict_parser: ClassFieldParser[OneTimeIncome] = class_dict_parser

    def get_one_time_income(self, dict_data: dict):
        keys_to_skip: list[str] = ['id', 'income_history']
        income: dict = {}
        print(dict_data)
        for key in self.class_dict_parser.get_class_fields():
            print(key)
            if key not in keys_to_skip:
                income[key] = self.parse(dict_data, key)
        one_time_income: OneTimeIncome = OneTimeIncome(**income)
        one_time_income.income_history = IncomeHistory()
        return one_time_income