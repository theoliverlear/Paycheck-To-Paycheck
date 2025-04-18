# session_service.py
import logging
from typing import Optional

from injector import inject

from backend.apps.entity.user.user import User
from backend.apps.services.user_service import UserService


class SessionService:

    @inject
    def __init__(self,
                 user_service: UserService):
        self.user_service: UserService = user_service

    async def get_user_from_session(self, http_request) -> Optional[User]:
        if not self.user_in_session(http_request):
            logging.warning("User ID not found in session.")
            return None
        user_id: int = http_request.session['user_id']
        return await self.user_service.get_by_id(user_id)

    def remove_user_from_session(self, http_request):
        if self.user_in_session(http_request):
            del http_request.session['user_id']

    def save_user_to_session(self, user: User, http_request) -> None:
        http_request.session['user_id'] = user.id

    def user_in_session(self, http_request) -> bool:
        user_id_key_exists: bool = 'user_id' in http_request.session
        return user_id_key_exists

    def get_session(self, http_request):
        return http_request.session