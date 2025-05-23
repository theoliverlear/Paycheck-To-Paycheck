from typing import override

from attr import attr
from attrs import define
from channels.db import database_sync_to_async

from backend.apps.entity.income.models import WageIncomeOrmModel
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.recurring_date import RecurringDate
from backend.apps.entity.time.year_interval import YearInterval
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class WageIncome(RecurringIncome, OrmCompatible['WageIncome', WageIncomeOrmModel]):
    weekly_hours: float = attr(default=0.0)

    def calculate_yearly_income(self):
        income_per_week: float = self._amount * self.weekly_hours
        self.yearly_income = income_per_week * YearInterval.WEEKLY.value

    def calculate_paycheck_income(self):
        income_per_week: float = self._amount * self.weekly_hours * 2
        return income_per_week

    @RecurringIncome.recurring_date.setter
    def recurring_date(self, recurring_date: RecurringDate):
        # TODO: Add more complex logic at some point to allow for different
        #       pay periods.
        same_interval: bool = recurring_date.interval == self._recurring_date.interval
        if not same_interval:
            raise ValueError("Wages are only paid bi-weekly.")
        else:
            RecurringIncome.recurring_date.fset(self, recurring_date)

    @override
    async def save(self) -> 'WageIncome':
        if self.is_initialized():
            self.update()
            return self
        else:
            saved_recurring_date: RecurringDate = await self._recurring_date.save()
            orm_model: WageIncomeOrmModel = self.get_orm_model()
            saved_wage_income: WageIncomeOrmModel = await database_sync_to_async(WageIncomeOrmModel.objects.create)(
                name=orm_model.name,
                amount=orm_model.amount,
                recurring_date=saved_recurring_date.get_orm_model(),
                weekly_hours=self.weekly_hours,
                income_history=self.income_history.get_orm_model()
            )
            self.set_from_orm_model(saved_wage_income)
            return WageIncome.from_orm_model(saved_wage_income)

    @override
    def update(self) -> None:
        try:
            db_model: WageIncomeOrmModel = WageIncomeOrmModel.objects.get(id=self.id)
            self._recurring_date.update()
            orm_model: WageIncomeOrmModel = self.get_orm_model()
            current_model: WageIncomeOrmModel = WageIncome.set_orm_model(db_model, orm_model)
            current_model.save()
        except WageIncomeOrmModel.DoesNotExist as exception:
            raise EntityNotFoundException(self)


    @override
    def set_from_orm_model(self, orm_model: WageIncomeOrmModel) -> None:
        from backend.apps.entity.income.income_history import IncomeHistory
        self.id = orm_model.id
        self.name = orm_model.name
        self.amount = orm_model.amount
        self.recurring_date = RecurringDate.from_orm_model(orm_model.recurring_date)
        self.weekly_hours = orm_model.weekly_hours
        self.income_history = IncomeHistory.from_orm_model(orm_model.income_history)

    @override
    def get_orm_model(self) -> WageIncomeOrmModel:
        return WageIncomeOrmModel(
            id=self.id,
            name=self.name,
            amount=self.amount,
            recurring_date=self._recurring_date.get_orm_model(),
            income_history=self.income_history.get_orm_model(),
            weekly_hours=self.weekly_hours
        )

    @override
    @staticmethod
    def set_orm_model(db_model: WageIncomeOrmModel,
                      model_to_match: WageIncomeOrmModel) -> WageIncomeOrmModel:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.amount = model_to_match.amount
        db_model.recurring_date = model_to_match.recurring_date
        db_model.income_history = model_to_match.income_history
        db_model.weekly_hours = model_to_match.weekly_hours
        return db_model

    @override
    @staticmethod
    def from_orm_model(orm_model: WageIncomeOrmModel) -> 'WageIncome':
        wage_income: WageIncome = WageIncome()
        wage_income.set_from_orm_model(orm_model)
        return wage_income
