from django.apps import AppConfig


class CommonsConfig(AppConfig):
    name = 'sgi.commons'
    label = 'sgi_commons'

    def ready(self):
        # print('sgi commons ready')
        pass
