from typing import override

from attr import attr
from attrs import define

from backend.apps.entity.holding.debt.models import DebtOrmModel
from backend.apps.entity.holding.holding import Holding
from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class Debt(Holding, OrmCompatible['Debt', DebtOrmModel]):
    @override
    def save(self) -> 'Debt':
        if self.is_initialized():
            self.update()
            return self
        else:
            saved_model: DebtOrmModel = DebtOrmModel.objects.create(
                name=self.name,
                amount=self.amount
            )
            return Debt.from_orm_model(saved_model)

    @override
    def update(self) -> None:
        try:
            db_model: DebtOrmModel = DebtOrmModel.objects.get(id=self.id)
            orm_model: DebtOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except DebtOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    @override
    def set_from_orm_model(self, orm_model: DebtOrmModel) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.amount = orm_model.amount

    @override
    def get_orm_model(self) -> DebtOrmModel:
        return DebtOrmModel(
            id=self.id,
            name=self.name,
            amount=self.amount
        )

    @staticmethod
    @override
    def set_orm_model(db_model: DebtOrmModel,
                      model_to_match: DebtOrmModel) -> None:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.amount = model_to_match.amount

    @staticmethod
    @override
    def from_orm_model(orm_model: DebtOrmModel) -> 'Debt':
        debt: Debt = Debt()
        debt.set_from_orm_model(orm_model)
        return debt