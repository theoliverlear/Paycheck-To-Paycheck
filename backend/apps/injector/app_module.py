from injector import Binder, singleton

from backend.apps.repository.user_repository import UserRepository
from backend.apps.services.auth_service import AuthService
from backend.apps.services.user_service import UserService

class AppModule:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def configure(self, binder: Binder):
        binder.bind(UserRepository, to=UserRepository, scope=singleton)
        binder.bind(UserService, to=UserService, scope=singleton)
        binder.bind(AuthService, to=AuthService, scope=singleton)