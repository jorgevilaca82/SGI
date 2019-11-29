from django.test import TestCase

# Create your tests here.

class HomeViewsTest(TestCase):
    
    def test_home_root_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)