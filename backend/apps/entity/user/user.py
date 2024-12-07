from abc import ABC

from attr import attr
from attrs import define

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.income.recurring_income import RecurringIncome
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.user.models import UserOrmModel, SafePasswordOrmModel
from backend.apps.entity.user.safe_password import SafePassword
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class User(OrmCompatible, ABC, Identifiable):
    first_name: str = attr(default="")
    last_name: str = attr(default="")
    username: str = attr(default="")
    recurring_income: RecurringIncome = attr(factory=RecurringIncome)
    password: SafePassword = attr(factory=SafePassword)

    def save(self):
        saved_recurring_income: RecurringIncome = self.recurring_income.save()
        saved_password: SafePassword = self.password.save()
        orm_model: UserOrmModel = self.get_orm_model()
        saved_user = UserOrmModel.objects.create(
            first_name=orm_model.first_name,
            last_name=orm_model.last_name,
            username=orm_model.username,
            recurring_income=saved_recurring_income.get_orm_model(),
            password=saved_password.get_orm_model()
        )
        return User.from_orm_model(saved_user)

    def update(self) -> None:
        try:
            db_model: UserOrmModel = UserOrmModel.objects.get(id=self.id)
            self.recurring_income.update()
            self.password.update()
            orm_model: UserOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except UserOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        self.first_name = orm_model.first_name
        self.last_name = orm_model.last_name
        self.username = orm_model.username
        self.recurring_income = RecurringIncome.from_orm_model(orm_model.recurring_income)
        self.password = SafePassword.from_orm_model(orm_model.password)

    @staticmethod
    def set_orm_model(db_model, model_to_match) -> None:
        db_model.id = model_to_match.id
        db_model.first_name = model_to_match.first_name
        db_model.last_name = model_to_match.last_name
        db_model.username = model_to_match.username
        db_model.recurring_income = model_to_match.recurring_income
        db_model.password = model_to_match.password

    def get_orm_model(self) -> UserOrmModel:
        return UserOrmModel(
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            recurring_income=self.recurring_income.get_orm_model(),
            password=self.password.get_orm_model()
        )

    @staticmethod
    def from_orm_model(orm_model: UserOrmModel) -> 'User':
        user: User = User()
        user.set_from_orm_model(orm_model)
        return user