from datetime import date
from typing import override

from djangorestframework_camel_case.util import underscoreize
from injector import inject

from backend.apps.entity.income.income_history import IncomeHistory
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.models.date_utilities import iso_to_django_date
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.dict_parser import DictParser


class RecurringIncomeDictParser(DictParser):
    @inject
    def __init__(self, class_dict_parser: ClassFieldParser[RecurringIncome]):
        self.class_dict_parser: ClassFieldParser[RecurringIncome] = class_dict_parser

    @override
    def parse(self, dict_data: dict, key: str) -> str | int | float | date:
        normalized_key: str = self.camel_to_snake(key)
        if self.is_interval_key(normalized_key):
            self.normalize_interval_key(dict_data, normalized_key)
            return dict_data['interval']
        else:
            return super().parse(dict_data, normalized_key)

    def is_interval_key(self, key) -> bool:
        return key == 'income_interval'

    def normalize_interval_key(self, dict_data: dict, key):
        dict_value: str = dict_data[key]
        dict_data['interval'] = dict_value

    def get_recurring_income(self, dict_data: dict) -> RecurringIncome:
        dict_data = underscoreize(dict_data)
        keys_to_skip: list[str] = ['id', 'income_history', 'recurring_date', 'yearly_income']
        income: dict = {}
        date_received: date = iso_to_django_date(dict_data['date_received'])
        year_interval: YearInterval = YearInterval.from_title(dict_data['income_interval'])
        income_recurring_date: RecurringDate = RecurringDate(day=date_received,
                                                             interval=year_interval)
        for key in self.class_dict_parser.get_class_fields():
            if key not in keys_to_skip:
                income[key] = self.parse(dict_data, key)
        recurring_income: RecurringIncome = RecurringIncome(**income)
        recurring_income.recurring_date = income_recurring_date
        recurring_income.income_history = IncomeHistory()
        return recurring_income

