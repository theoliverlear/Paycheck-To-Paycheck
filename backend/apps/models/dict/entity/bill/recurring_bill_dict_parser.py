from datetime import date

from djangorestframework_camel_case.util import underscoreize
from injector import inject

from backend.apps.entity.bill.bill_history import BillHistory
from backend.apps.entity.bill.recurring_bill import RecurringBill
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.models.dict.class_field_parser import ClassFieldParser
from backend.apps.models.dict.dict_parser import DictParser


class RecurringBillDictParser(DictParser):
    @inject
    def __init__(self, class_dict_parser: ClassFieldParser[RecurringBill]):
        self.class_dict_parser: ClassFieldParser[RecurringBill] = class_dict_parser

    def get_recurring_bill(self, dict_data: dict) -> RecurringBill:
        dict_data = underscoreize(dict_data)
        dict_data['recurring_date'] = dict_data['date']
        keys_to_skip: list[str] = ['id', 'bill_history', 'bill_interval']
        bill_dict: dict = {}
        for key in self.class_dict_parser.get_class_fields():
            if key not in keys_to_skip:
                bill_dict[key] = self.parse(dict_data, key)
                if isinstance(bill_dict[key], date):
                    if 'bill_interval' not in dict_data:
                        bill_interval: YearInterval = YearInterval.MONTHLY
                    else:
                        bill_interval: YearInterval = self.interval_text_to_enum(dict_data['bill_interval'])
                    bill_dict[key] = RecurringDate(day=bill_dict[key],
                                                   interval=bill_interval)
        recurring_bill: RecurringBill = RecurringBill(**bill_dict)
        recurring_bill.bill_history = BillHistory()
        return recurring_bill


    def interval_text_to_enum(self, bill_interval: str) -> YearInterval:
        match bill_interval:
            case 'Monthly':
                return YearInterval.MONTHLY
            case 'Yearly':
                return YearInterval.YEARLY
            case 'Bi-Weekly':
                return YearInterval.BI_WEEKLY
            case 'Weekly':
                return YearInterval.WEEKLY
            case 'Quarterly':
                return YearInterval.QUARTERLY
            case 'Daily':
                return YearInterval.DAILY
            case _:
                raise ValueError(f"Invalid interval: {bill_interval}")

