from django.apps import AppConfig


class ServiceappConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
