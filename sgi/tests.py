from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
from django.test import TestCase


class StaticFilesTest(TestCase):
    pass
    # ainda não funciona
    # def test_static_exists_at_desired_location(self):
    #     absolute_path = finders.find('img/sapo.jpg')
    #     assert staticfiles_storage.exists(absolute_path)
