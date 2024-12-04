import bcrypt
from attr import attr
from attrs import define


@define(init=False)
class SafePassword:
    encoded_password: str = attr(default='')
    ENCODING_TYPE: str = 'utf-8'
    def __init__(self, unhashed_password: str=''):
        self.encoded_password = self.hash_password(unhashed_password)

    def set_new_unhashed_password(self, unhashed_password: str):
        self.encoded_password = self.hash_password(unhashed_password)

    def hash_password(self, unhashed_password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(unhashed_password.encode(self.ENCODING_TYPE), salt)
        return hashed_password.decode(self.ENCODING_TYPE)

    def compare_unencoded_password(self, unencoded_password: str) -> bool:
        return bcrypt.checkpw(unencoded_password.encode(self.ENCODING_TYPE), self.encoded_password.encode(self.ENCODING_TYPE))