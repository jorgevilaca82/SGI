from django.test import TestCase
from .models import UnidadeDeEnsino, AreaUnidadeDeEnsino
from sgi.base.models import PessoaFisica

# Create your tests here.

class UnidadesAreasAcademicasTest(TestCase):

    def test_create_unidade_de_ensino(self):
        
        campus1 = UnidadeDeEnsino.objects.create(
            tipo=UnidadeDeEnsino.Tipo.CAMPUS, 
            sigla='PVHCAL', 
            nome='CAMPUS PVH CALAMA'
        )

        self.assertIsNot(campus1.pk, None)

        polo1 = UnidadeDeEnsino.objects.create(
            tipo=UnidadeDeEnsino.Tipo.POLO, 
            sigla='POLO_VLH', 
            nome='POLO VILHENA'
        )

        self.assertIsNot(polo1.pk, None)


        responsavel = PessoaFisica.objects.create(nome='Jorge Vilaca', cpf='70434239291')


        area_diretoria = AreaUnidadeDeEnsino.objects.create(
            tipo=AreaUnidadeDeEnsino.Tipo.DIRETORIA_DE_ENSINO, 
            sigla='DECAL', 
            nome='DIRETORIA DE ENSINO PVHCAL'
        )

        self.assertIsNot(area_diretoria.pk, None)
        
        area_diretoria.responsavel = responsavel
        area_diretoria.unidade_de_ensino = campus1
        area_diretoria.save()

        self.assertEqual(area_diretoria.unidade_de_ensino.pk, campus1.pk)
        self.assertEqual(area_diretoria.responsavel.pk, responsavel.pk)
