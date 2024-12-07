from django.urls import path

from backend.apps.views.user.user_view import UserView

urlpatterns = [
    path('<int:params>', UserView.as_view(), name='user_view'),
]