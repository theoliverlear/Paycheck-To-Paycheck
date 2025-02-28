import logging
from datetime import date

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.models.date_utilities import get_next_bi_week


@define
class DateRange(Identifiable):
    starting_date: date = attr(default=date.today())
    ending_date: date = attr(default=get_next_bi_week(date.today()))

    def in_range(self, date_to_check: date) -> bool:
        return self.starting_date <= date_to_check <= self.ending_date

    def print_in_range(self, date_to_check: date) -> None:
        in_range: bool = self.in_range(date_to_check)
        logging.info(f'The date range starting {self.starting_date} to {self.ending_date} is in range of {date_to_check}: {in_range}')