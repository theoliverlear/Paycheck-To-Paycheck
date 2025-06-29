from django.urls import path, include

urlpatterns = [
    path('authorize/', include('backend.apps.views.authorize.urls')),
    path('bill/', include('backend.apps.views.bill.urls')),
    path('income/', include('backend.apps.views.income.urls')),
    path('paycheck/', include('backend.apps.views.paycheck.urls')),
    path('user/', include('backend.apps.views.user.urls')),
    path('wallet/', include('backend.apps.views.wallet.urls')),
    path('welcome/', include('backend.apps.views.welcome.urls'))
]