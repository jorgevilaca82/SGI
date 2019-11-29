from django.conf import settings


def app_settings(request):
    default_layout = 'layout.html'

    if hasattr(settings, 'DEFAULT_LAYOUT'):
        default_layout = settings.DEFAULT_LAYOUT

    return {
        'app_name': settings.APP_NAME,
        'default_layout': default_layout
    }
