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