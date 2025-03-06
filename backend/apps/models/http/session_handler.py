from abc import ABC, abstractmethod

from attrs import define

from backend.apps.entity.user.user import User

# TODO: Implement this interface.
@define
class SessionHandler(ABC):
    @abstractmethod
    def save_user_to_session(self, user: User):
        pass