from django.core.exceptions import ValidationError
from django.test import TestCase

from sgi.base.models import *


class UnidadeOrganizacionalTestCase(TestCase):

    fixtures = (
        "pessoas.yaml",
        "pessoasjuridicas.yaml",
    )

    def setUp(self):
        self.pessoa_juridica = PessoaJuridica.objects.get(pk=2)

        self.uo_reitoria = UnidadeOrganizacional.objects.create(
            sigla="REITORIA", nome="REITORIA", pessoa_juridica=self.pessoa_juridica
        )

        self.dgti = UnidadeOrganizacional(
            sigla="DGTI",
            nome="Diretoria de Gestão de Tecnologia da Informação",
            pessoa_juridica=self.pessoa_juridica,
        )

        self.dgti.save()

    def test_create_unidade_organizacional_com_pj(self):

        self.assertIsNotNone(self.pessoa_juridica)
        self.assertIsInstance(self.pessoa_juridica, PessoaJuridica)
        self.assertIsNotNone(self.uo_reitoria)
        self.assertIsInstance(self.uo_reitoria, UnidadeOrganizacional)

    def test_fail_create_unidade_organizacional(self):

        # with self.assertRaises(ValidationError) as cm:
        self.dgti.full_clean()

        # ex = cm.exception
        # self.assertIsInstance(ex, ValidationError)

        # self.assertEqual(the_exception.error_code, 3)
        # dgti não está atrelada nem a uma PJ e nem a uma unidade superior
        # self.assertTrue('__all__' in ex)
        # self.assertEqual(ex['__all__'][0], 'xUnidade Organizacional deve estar atrelada à uma pessoa jurídica ou à uma unidade organizacional superior.')

    def test_associacao_uos(self):
        self.uo_reitoria.subordinados.add(self.dgti)
