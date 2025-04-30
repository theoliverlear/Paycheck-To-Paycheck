from django.urls import path

from backend.apps.views.authorize.is_logged_in_view import IsLoggedInView
from backend.apps.views.authorize.login_view import LoginView
from backend.apps.views.authorize.logout_view import LogoutView
from backend.apps.views.authorize.signup_view import SignupView

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('signup', SignupView.as_view(), name="signup"),
    path('isloggedin', IsLoggedInView.as_view(), name="isloggedin"),
    path('logout', LogoutView.as_view(), name="logout"),
]