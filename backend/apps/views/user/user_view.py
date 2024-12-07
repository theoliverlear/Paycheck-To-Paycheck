from django.http import HttpResponse
from injector import inject
from rest_framework.views import APIView

from backend.apps.entity.user.user import User
from backend.apps.services.user_service import UserService


class UserView(APIView):
    @inject
    def __init__(self, user_service: UserService):
        super().__init__()
        self.user_service = user_service

    def get(self, request, params, *args, **kwargs):
        user: User = self.user_service.user_repository.get_by_id(params)
        return HttpResponse(user)
