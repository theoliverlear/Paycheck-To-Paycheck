from attr import attr
from attrs import define

from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.bill.recurring_bill import RecurringBill


@define
class BillsResponse:
    one_time_bills: list[OneTimeBill] = attr(default=[])
    recurring_bills: list[RecurringBill] = attr(default=[])