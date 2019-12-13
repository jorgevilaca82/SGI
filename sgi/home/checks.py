from django.apps import apps
from django.core.checks import Error, register


@register()
def sgi_commons_installed_check(app_configs, **kwargs):
    errors = []
    if apps.is_installed('sgi_commons'):
        errors.append(
            Error(
                'SGI Commons não está instalado',
                hint='Adicione ao settings.INSTALLED_APPS o app sgi.commons.',
                obj=None,
                id='sgi_home.E001',
            )
        )
    return errors
