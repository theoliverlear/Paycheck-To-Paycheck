from abc import ABC
from typing import Optional

from backend.apps.entity.identifiable import Identifiable
from backend.apps.entity.user.models import UserOrmModel
from backend.apps.entity.user.user import User
from backend.apps.repository.database_accessible import DatabaseAccessible, T


class UserRepository(DatabaseAccessible, ABC):
    def get_user_by_username(self, username: str) -> Optional[User]:
        users_with_username = UserOrmModel.objects.filter(username=username)
        if not users_with_username:
            return None
        user: User = User.from_orm_model(users_with_username.first())
        return user

    def exists_by_id(self, identifiable: Identifiable | int) -> bool:
        id_num: int = 0
        if isinstance(identifiable, Identifiable):
            id_num = identifiable.id
        else:
            id_num = identifiable
        return UserOrmModel.objects.filter(id=id_num).exists()

    def save_or_update_user(self, user: User) -> Optional[User]:
        if self.exists_by_id(user):
            self.update(user)
            return None
        else:
            return self.save(user)

    def get_by_id(self, identifiable: Identifiable | int) -> T:
        id_num: int = 0
        if isinstance(identifiable, Identifiable):
            id_num = identifiable.id
        else:
            id_num = identifiable
        user_orm_model = UserOrmModel.objects.get(id=id_num)
        return User.from_orm_model(user_orm_model)
    def save(self, user: User) -> User:
        return user.save()

    def update(self, user: User) -> None:
        user.update()