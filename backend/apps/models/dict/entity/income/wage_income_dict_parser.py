from datetime import date

from injector import inject

from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.models.date_utilities import iso_to_django_date
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.dict_parser import DictParser
from backend.apps.entity.income.income_history import IncomeHistory


class WageIncomeDictParser(DictParser):
    @inject
    def __init__(self,
                 class_dict_parser: ClassFieldParser[WageIncome]):
        self.class_dict_parser: ClassFieldParser[WageIncome] = class_dict_parser

    def get_wage_income(self, dict_data: dict):
        keys_to_skip: list[str] = ['id', 'income_history', 'recurring_date', 'yearly_income']
        income: dict = {}
        date_received: date = iso_to_django_date(dict_data['date_received'])
        year_interval: YearInterval = YearInterval.from_title(dict_data['income_interval'])
        income_recurring_date: RecurringDate = RecurringDate(day=date_received,
                                                             interval=year_interval)
        for key in self.class_dict_parser.get_class_fields():
            if key not in keys_to_skip:
                income[key] = self.parse(dict_data, key)
        wage_income: WageIncome = WageIncome(**income)
        wage_income.recurring_date = income_recurring_date
        wage_income.income_history = IncomeHistory()
        return wage_income