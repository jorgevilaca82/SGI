from django.apps import AppConfig


class AcademicoConfig(AppConfig):
    name = 'sgi.academico'

    def ready(self):
        from . import signals
        from . import di # dependency injection
