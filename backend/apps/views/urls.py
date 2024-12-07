from django.urls import path, include

from backend.apps.views.home_view import HomeView

urlpatterns = [
    path('<str:param>', HomeView.as_view(), name='home'),
    path('paycheck/', include('apps.views.paycheck.urls')),
    path('user/', include('apps.views.user.urls')),
]