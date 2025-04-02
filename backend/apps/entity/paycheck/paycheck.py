import logging

from attr import attr
from attrs import define

from backend.apps.entity.bill.one_time_bill import OneTimeBill
from backend.apps.entity.bill.recurring_bill import RecurringBill
from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.one_time_income import OneTimeIncome
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.income.wage_income import WageIncome
from backend.apps.entity.time.date_range import DateRange
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.entity.user.user import User


@define
class Paycheck(Identifiable):
    _date_range: DateRange = attr(factory=DateRange)
    one_time_incomes: list[OneTimeIncome] = attr(default=[])
    recurring_incomes: list[RecurringIncome] = attr(default=[])
    wage_incomes: list[WageIncome] = attr(default=[])
    one_time_bills: list[OneTimeBill] = attr(default=[])
    recurring_bills: list[RecurringBill] = attr(default=[])
    total_income: float = attr(default=0.0)
    total_bills: float = attr(default=0.0)
    left_over_income: float = attr(default=0.0)

    def calculate_leftover_income(self):
        self.left_over_income = self.total_income - self.total_bills

    @property
    def date_range(self):
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        self._date_range = date_range
        self.purge_outdated_items()

    def __attrs_post_init__(self):
        self.update_totals()

    @staticmethod
    def from_user(user: User):
        paycheck: Paycheck = Paycheck()
        paycheck.one_time_incomes = user.income_history.one_time_incomes
        paycheck.recurring_incomes = user.income_history.recurring_incomes
        paycheck.wage_incomes = user.income_history.wage_incomes
        paycheck.one_time_bills = user.bill_history.one_time_bills
        paycheck.recurring_bills = user.bill_history.recurring_bills
        paycheck.purge_outdated_items()
        return paycheck

    def purge_outdated_items(self):
        self.purge_outdated_incomes()
        self.purge_outdated_bills()
        self.update_totals()

    def update_totals(self):
        self.update_total_income()
        self.update_total_bills()
        self.calculate_leftover_income()

    def update_total_income(self):
        self.total_income = self.get_total_income()

    def update_total_bills(self):
        self.total_bills = self.get_total_bills()

    def get_num_incomes(self) -> int:
        return len(self.one_time_incomes) + len(self.recurring_incomes) + len(self.wage_incomes)

    def get_num_bills(self) -> int:
        return len(self.one_time_bills) + len(self.recurring_bills)

    def add_one_time_income(self, one_time_income: OneTimeIncome) -> None:
        contains_income: bool = one_time_income in self.one_time_incomes
        self._date_range.print_in_range(one_time_income.date_received)
        in_range: bool = self._date_range.in_range(one_time_income.date_received)
        logging.info(f'One time income --- In range: {in_range}, Contains income {contains_income}')
        if not contains_income and in_range:
            self.one_time_incomes.append(one_time_income)
            self.update_total_income()
            self.purge_outdated_incomes()

    def add_recurring_income(self, recurring_income: RecurringIncome) -> None:
        contains_income: bool = recurring_income in self.recurring_incomes
        in_range: bool = self._date_range.in_range(recurring_income.recurring_date.day)
        if not contains_income and in_range:
            self.recurring_incomes.append(recurring_income)
            self.update_total_income()
            self.purge_outdated_incomes()

    def add_wage_income(self, wage_income: WageIncome):
        contains_income: bool = wage_income in self.wage_incomes
        in_range: bool = self._date_range.in_range(wage_income.recurring_date.day)
        if not contains_income and in_range:
            self.wage_incomes.append(wage_income)
            self.update_total_income()
            self.purge_outdated_incomes()

    def add_one_time_bill(self, one_time_bill: OneTimeBill) -> None:
        contains_bill: bool = one_time_bill in self.one_time_bills
        in_range: bool = self._date_range.in_range(one_time_bill.due_date.due_date)
        if not contains_bill and in_range:
            self.one_time_bills.append(one_time_bill)
            self.update_total_bills()
            self.purge_outdated_bills()

    def add_recurring_bill(self, recurring_bill: RecurringBill) -> None:
        contains_bill: bool = recurring_bill in self.recurring_bills
        in_range: bool = self._date_range.in_range(recurring_bill.recurring_date.day)
        if not contains_bill and in_range:
            self.recurring_bills.append(recurring_bill)
            self.update_total_bills()
            self.purge_outdated_bills()

    def get_total_income(self):
        total_yearly_income: float = 0.0
        for recurring_income in self.recurring_incomes:
            total_yearly_income += recurring_income.yearly_income
        for wage_income in self.wage_incomes:
            total_yearly_income += wage_income.yearly_income
        total_yearly_income /= YearInterval.BI_WEEKLY.value
        for one_time_income in self.one_time_incomes:
            total_yearly_income += one_time_income.income_amount
        return total_yearly_income

    def get_total_bills(self):
        total_bills: float = 0.0
        for one_time_bill in self.one_time_bills:
            total_bills += one_time_bill.amount
        for recurring_bill in self.recurring_bills:
            total_bills += recurring_bill.amount
        return total_bills

    @staticmethod
    def income_to_paycheck(yearly_income: float) -> float:
        return yearly_income / YearInterval.BI_WEEKLY.value

    def print_all_incomes(self) -> None:
        for one_time_income in self.one_time_incomes:
            logging.info(f'One time income - {one_time_income.name}: ${one_time_income.income_amount}')
        for recurring_income in self.recurring_incomes:
            paycheck_income: float = recurring_income.yearly_income / YearInterval.BI_WEEKLY.value
            logging.info(f'Recurring income - {recurring_income.name}: ${paycheck_income}')
        for wage_income in self.wage_incomes:
            paycheck_income = wage_income.income_amount * wage_income.weekly_hours * 2
            logging.info(f'Wage income - {wage_income.name}: ${paycheck_income}')

    def purge_outdated_incomes(self):
        # TODO: Reduce boilerplate by passing each section into a single
        #       method.
        updated_one_time_incomes: list[OneTimeIncome] = []
        for one_time_income in self.one_time_incomes:
            contains_income = one_time_income in updated_one_time_incomes
            if self._date_range.in_range(one_time_income.date_received) and not contains_income:
                updated_one_time_incomes.append(one_time_income)
        self.one_time_incomes = updated_one_time_incomes

        updated_recurring_incomes: list[RecurringIncome] = []
        for recurring_income in self.recurring_incomes:
            contains_income = recurring_income in updated_recurring_incomes
            if self._date_range.in_range(recurring_income.recurring_date.day) and not contains_income:
                updated_recurring_incomes.append(recurring_income)
        self.recurring_incomes = updated_recurring_incomes

        updated_wage_incomes: list[WageIncome] = []
        for wage_income in self.wage_incomes:
            contains_income = wage_income in updated_wage_incomes
            if self._date_range.in_range(wage_income.recurring_date.day) and not contains_income:
                updated_wage_incomes.append(wage_income)
        self.wage_incomes = updated_wage_incomes
        self.update_total_income()


    def purge_outdated_bills(self):
        updated_one_time_bills: list[OneTimeBill] = []
        for one_time_bill in self.one_time_bills:
            contains_bill = one_time_bill in updated_one_time_bills
            if self._date_range.in_range(one_time_bill.due_date.due_date) and not contains_bill:
                updated_one_time_bills.append(one_time_bill)
        self.one_time_bills = updated_one_time_bills

        updated_recurring_bills: list[RecurringBill] = []
        for recurring_bill in self.recurring_bills:
            contains_bill = recurring_bill in updated_recurring_bills
            if self._date_range.in_range(recurring_bill.recurring_date.day) and not contains_bill:
                updated_recurring_bills.append(recurring_bill)
        self.recurring_bills = updated_recurring_bills
        self.update_total_bills()

    def remove_one_time_income(self, income_title: str):
        for index, one_time_income in enumerate(self.one_time_incomes):
            if one_time_income.name == income_title:
                self.one_time_incomes.pop(index)