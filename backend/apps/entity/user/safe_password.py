from abc import ABC
from typing import override

import bcrypt
from attr import attr
from channels.db import database_sync_to_async

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.user.models import SafePasswordOrmModel
from backend.apps.exception.entity_not_found_exception import \
    EntityNotFoundException


class SafePassword(OrmCompatible['SafePassword', SafePasswordOrmModel], ABC, Identifiable):
    encoded_password: str = attr(default='')
    ENCODING_TYPE = 'utf-8'
    def __init__(self, id: int = 0, unhashed_password: str=''):
        self._id = id
        self.encoded_password = self.hash_password(unhashed_password)

    def set_new_unhashed_password(self, unhashed_password: str):
        self.encoded_password = self.hash_password(unhashed_password)

    def hash_password(self, unhashed_password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(unhashed_password.encode(SafePassword.ENCODING_TYPE), salt)
        return hashed_password.decode(SafePassword.ENCODING_TYPE)

    def compare_unencoded_password(self, unencoded_password: str) -> bool:
        return bcrypt.checkpw(unencoded_password.encode(SafePassword.ENCODING_TYPE), self.encoded_password.encode(SafePassword.ENCODING_TYPE))

    @override
    async def save(self) -> 'SafePassword':
        orm_model: SafePasswordOrmModel = self.get_orm_model()
        saved_password = await database_sync_to_async(SafePasswordOrmModel.objects.create)(
            encoded_password=orm_model.encoded_password
        )
        return SafePassword.from_orm_model(saved_password)

    @override
    def update(self) -> None:
        try:
            db_model = SafePasswordOrmModel.objects.get(id=self._id)

            orm_model = self.get_orm_model()
            self.set_orm_model(db_model, orm_model)
            db_model.save()
        except SafePasswordOrmModel.DoesNotExist:
            raise EntityNotFoundException(self)

    @override
    @staticmethod
    def set_orm_model(db_model, model_to_match) -> None:
        db_model.encoded_password = model_to_match.encoded_password

    @override
    def get_orm_model(self) -> SafePasswordOrmModel:
        return SafePasswordOrmModel(
            id=self.id,
            encoded_password=self.encoded_password
        )

    @override
    def set_from_orm_model(self, orm_model) -> None:
        self.id = orm_model.id
        self.encoded_password = orm_model.encoded_password

    @override
    @staticmethod
    def from_orm_model(orm_model: SafePasswordOrmModel) -> 'SafePassword':
        safe_password = SafePassword()
        safe_password.set_from_orm_model(orm_model)
        return safe_password