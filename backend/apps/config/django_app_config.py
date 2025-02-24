from django.apps import AppConfig
from injector import Injector

from backend.apps.injector import AppModule


class DjangoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

    def ready(self):
        injector = Injector([AppModule()])