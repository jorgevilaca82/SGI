from enum import Enum

from django.db import models
from django.utils.translation import gettext_lazy as _

from sgi.base import models as bm


class SetorTipo(models.Model):
    
    class Meta:
        pass

    nome = models.CharField(max_length=255)


class Setor(bm.UnidadeOrganizacional):
    
    class Meta:
        pass

    class Categoria(Enum):
        ADMINISTRATIVO = 'ADM'
        FINANCEIRO = 'FIN'
        RECURSOS_HUMANOS = 'RH'
        OPERACIONAL = 'OPR'
        COMERCIAL = 'COM'

    CATEGORIA_CHOICES = (
        (Categoria.ADMINISTRATIVO.value, _('ADMINISTRATIVO')),
        (Categoria.FINANCEIRO.value, _('FINANCEIRO')),
        (Categoria.RECURSOS_HUMANOS.value, _('RECURSOS_HUMANOS')),
        (Categoria.OPERACIONAL.value, _('OPERACIONAL')),
        (Categoria.COMERCIAL.value, _('COMERCIAL')),
    )

    CATEGORIA_DEFAULT = Categoria.ADMINISTRATIVO

    categoria = models.IntegerField(choices=CATEGORIA_CHOICES)

    responsavel = models.ForeignKey(bm.PessoaFisica, on_delete=models.PROTECT)

    tipo = models.ForeignKey(SetorTipo, on_delete=models.PROTECT)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.pk and not self.categoria:
            self.categoria = self.CATEGORIA_DEFAULT

    def __str__(self):
        return super().__str__()
