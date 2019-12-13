from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from sgi.base import models as bm
from sgi.commons.models import AuditableModel


class UnidadeOrganizacional(AuditableModel):

    class Meta:
        verbose_name = _('Unidade Organizacional')
        verbose_name_plural = _('Unidades Organizacionais')

    sigla = models.CharField(max_length=20)

    nome = models.CharField(max_length=140)

    # TODO: futuro implementar o campo e nas urls
    # slug = models.SlugField()

    # opcional no caso de sub unidades
    pessoa_juridica = models.ForeignKey(
        bm.PessoaJuridica, on_delete=models.PROTECT, blank=True, null=True)

    uo_superior = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='subordinados')

    def __str__(self):
        return '{0} > {1}'.format(
            (self.uo_superior or self.pessoa_juridica.razao_social or '!'),
            self.sigla)

    def clean(self):
        if not self.pessoa_juridica and not self.uo_superior:
            raise ValidationError(
                ('Unidade Organizacional deve estar atrelada à uma '
                 'pessoa jurídica ou à uma unidade organizacional superior.'))
