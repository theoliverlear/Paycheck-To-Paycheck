from django.urls import path, include

from backend.apps.views.home_view import HomeView

urlpatterns = [
    path('<str:param>', HomeView.as_view(), name='home'),
    path('paycheck/', include('backend.apps.views.paycheck.urls')),
    path('user/', include('backend.apps.views.user.urls')),
]