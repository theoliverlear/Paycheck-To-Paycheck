from attr import attr
from attrs import define

from backend.apps.entity.bill.models import OneTimeBillOrmModel
from backend.apps.entity.bill.undated_bill import UndatedBill
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.due_date import DueDate
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class OneTimeBill(UndatedBill, OrmCompatible['OneTimeBill', OneTimeBillOrmModel]):
    due_date: DueDate = attr(factory=DueDate)

    def save(self) -> 'OneTimeBill':
        saved_due_date: DueDate = self.due_date.save()
        orm_model: OneTimeBillOrmModel = self.get_orm_model()
        saved_bill: OneTimeBillOrmModel = OneTimeBillOrmModel.objects.create(
            name=orm_model.name,
            amount=orm_model.amount,
            due_date=DueDate.get_orm_model(saved_due_date)
        )
        return OneTimeBill.from_orm_model(saved_bill)

    def update(self) -> None:
        try:
            db_model: OneTimeBillOrmModel = OneTimeBillOrmModel.objects.get(id=self.id)
            self.due_date.update()
            orm_model: OneTimeBillOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except OneTimeBillOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    def set_from_orm_model(self, orm_model: OneTimeBillOrmModel) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.amount = orm_model.amount
        self.due_date = DueDate.from_orm_model(orm_model.due_date)

    def get_orm_model(self) -> OneTimeBillOrmModel:
        return OneTimeBillOrmModel(
            id=self.id,
            name=self.name,
            amount=self.amount,
            due_date=self.due_date.get_orm_model()
        )

    @staticmethod
    def set_orm_model(db_model: OneTimeBillOrmModel,
                      model_to_match: OneTimeBillOrmModel) -> None:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.amount = model_to_match.amount
        db_model.due_date = model_to_match.due_date

    @staticmethod
    def from_orm_model(orm_model: OneTimeBillOrmModel) -> 'OneTimeBill':
        bill = OneTimeBill()
        bill.set_from_orm_model(orm_model)
        return bill