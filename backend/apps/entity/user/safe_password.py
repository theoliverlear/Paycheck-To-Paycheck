from abc import ABC

import bcrypt
from django.db import models

from backend.apps.entity.orm_compatible import OrmCompatible
from backend.apps.entity.user.models import SafePasswordOrmModel


class SafePassword(OrmCompatible, ABC):
    encoded_password = models.CharField(max_length=100)
    ENCODING_TYPE = 'utf-8'
    def __init__(self, unhashed_password: str=''):
        super().__init__()
        self.encoded_password = self.hash_password(unhashed_password)

    def set_new_unhashed_password(self, unhashed_password: str):
        self.encoded_password = self.hash_password(unhashed_password)

    def hash_password(self, unhashed_password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(unhashed_password.encode(SafePassword.ENCODING_TYPE), salt)
        return hashed_password.decode(SafePassword.ENCODING_TYPE)

    def compare_unencoded_password(self, unencoded_password: str) -> bool:
        return bcrypt.checkpw(unencoded_password.encode(SafePassword.ENCODING_TYPE), self.encoded_password.encode(SafePassword.ENCODING_TYPE))

    def save(self):
        orm_model: SafePasswordOrmModel = self.get_orm_model()
        orm_model.save()

    def get_orm_model(self):
        return SafePasswordOrmModel(
            encoded_password=self.encoded_password
        )

    def set_from_orm_model(self, orm_model):
        self.encoded_password = orm_model.encoded_password


