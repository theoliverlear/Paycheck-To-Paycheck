from datetime import date

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable


@define
class DueDate(Identifiable):
    due_date: date = attr(default=date.today())

    def is_due(self, date_to_check: date) -> bool:
        return self.due_date <= date_to_check

    def is_overdue(self, date_to_check: date) -> bool:
        return self.due_date < date_to_check

    def not_yet_due(self, date_to_check: date) -> bool:
        return self.due_date > date_to_check