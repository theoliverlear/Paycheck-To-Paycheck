from django.urls import path

from backend.apps.views.wallet.set_wallet_view import SetWalletView

urlpatterns = [
    path('wallet', SetWalletView.as_view(), name='wallet')
]