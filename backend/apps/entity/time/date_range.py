import logging
from datetime import date

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.models.date_utilities import get_next_bi_week


@define
class DateRange(Identifiable):
    start_date: date = attr(default=date.today())
    end_date: date = attr(default=get_next_bi_week(date.today()))

    def in_range(self, date_to_check: date) -> bool:
        return self.start_date <= date_to_check <= self.end_date

    def print_in_range(self, date_to_check: date) -> None:
        in_range: bool = self.in_range(date_to_check)
        in_range_data: str = (f'The date range starting {self.start_date} to'
                              f' {self.end_date} is in range of'
                              f' {date_to_check}: {in_range}')
        logging.info(in_range_data)

    @staticmethod
    def get_paycheck_range(start_date: date):
        return DateRange(start_date=start_date,
                         end_date=get_next_bi_week(start_date))