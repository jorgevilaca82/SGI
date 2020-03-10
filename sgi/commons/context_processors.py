from django.conf import settings as s


def app_settings(request):
    return {"app_name": s.APP_NAME, "default_layout": s.DEFAULT_LAYOUT}
