from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.user.models import UserOrmModel
from backend.apps.entity.user.safe_password import SafePassword


@define
class User(OrmCompatible, ABC):
    first_name: str = attr(default="")
    last_name: str = attr(default="")
    username: str = attr(default="")
    recurring_income: RecurringIncome = attr(factory=RecurringIncome)
    password: SafePassword = attr(factory=SafePassword)

    def save(self):
        orm_model: UserOrmModel = self.get_orm_model()
        orm_model.save()

    def set_from_orm_model(self, orm_model):
        self.first_name = orm_model.first_name
        self.last_name = orm_model.last_name
        self.username = orm_model.username
        self.recurring_income = orm_model.recurring_income
        self.password = orm_model.password

    def get_orm_model(self):
        return UserOrmModel(
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            recurring_income=self.recurring_income.get_orm_model(),
            password=self.password.get_orm_model()
        )