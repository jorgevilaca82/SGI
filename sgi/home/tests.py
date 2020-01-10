from django.test import TestCase
from django.urls import reverse


class HomeViewsTest(TestCase):

    def test_home_root_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('dias_da_semana' in response.context)
        self.assertEqual(
            response.context['dias_da_semana'],
            [
                'Segunda',
                'Terça',
                'Quarta',
                'Quinta',
                'Sexta',
                'Sábado',
                'Domingo'
            ]
        )
