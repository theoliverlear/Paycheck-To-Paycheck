from attr import attr
from attrs import define

from backend.apps.entity.bill.models import BillOrmModel
from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.time.due_date import DueDate
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


@define
class Bill(Identifiable, OrmCompatible['Bill', BillOrmModel]):
    name: str = attr(default="")
    amount: float = attr(default=0.0)
    due_date: DueDate = attr(factory=DueDate)

    def save(self) -> 'Bill':
        saved_due_date: DueDate = self.due_date.save()
        orm_model: BillOrmModel = self.get_orm_model()
        saved_bill = BillOrmModel.objects.create(
            name=orm_model.name,
            amount=orm_model.amount,
            due_date=saved_due_date.get_orm_model()
        )
        return Bill.from_orm_model(saved_bill)

    def update(self) -> None:
        try:
            db_model: BillOrmModel = BillOrmModel.objects.get(id=self.id)
            self.due_date.update()
            orm_model: BillOrmModel = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except BillOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    def set_from_orm_model(self, orm_model: BillOrmModel) -> None:
        self.id = orm_model.id
        self.name = orm_model.name
        self.amount = orm_model.amount
        self.due_date = DueDate.from_orm_model(orm_model.due_date)

    def get_orm_model(self) -> BillOrmModel:
        return BillOrmModel(
            id=self.id,
            name=self.name,
            amount=self.amount,
            due_date=self.due_date.get_orm_model()
        )

    @staticmethod
    def set_orm_model(db_model: BillOrmModel, model_to_match: BillOrmModel) -> None:
        db_model.id = model_to_match.id
        db_model.name = model_to_match.name
        db_model.amount = model_to_match.amount
        db_model.due_date = model_to_match.due_date

    @staticmethod
    def from_orm_model(orm_model: BillOrmModel) -> 'Bill':
        bill = Bill()
        bill.set_from_orm_model(orm_model)
        return bill