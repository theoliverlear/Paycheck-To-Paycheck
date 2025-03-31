from asgiref.sync import sync_to_async
from attrs import define
from django.utils.functional import LazyObject

from backend.apps.entity.user.user import User


@define
class WebSocketSessionService:

    def get_session(self, session_scope: dict):
        session = session_scope.get("session")
        if session and isinstance(session, LazyObject):
            return session
        return None

    async def get_value(self, session_scope: dict, key):
        session = self.get_session(session_scope)
        if session:
            return session.get(key)
        return None

    async def set_value(self, session_scope: dict, key, value):
        session = self.get_session(session_scope)
        if session:
            session[key] = value
            await self.save_session(session)

    async def save_session(self, session):
        await sync_to_async(session.save)()

    async def user_in_session(self, session_scope) -> bool:
        user_value = await self.get_value(session_scope, "user_id")
        return user_value is not None

    async def save_user_to_session(self, session_scope, user: User):
        await self.set_value(session_scope, "user_id", user.id)

    async def remove_user_from_session(self, session_scope):
        await self.set_value(session_scope,"user_id", None)