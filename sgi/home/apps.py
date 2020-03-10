from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = "sgi.home"

    def ready(self):
        from . import checks
