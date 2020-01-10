from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.br import models as lf_models

from sgi.base.models import Pessoa


class PessoaJuridica(Pessoa):

    class Meta:
        verbose_name = _('Pessoa Jurídica')
        verbose_name_plural = _('Pessoas Jurídicas')

    cnpj = lf_models.BRCNPJField(unique=True)

    matriz = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='filiais')

    @property
    def razao_social(self):
        return self.nome_razao_social

    @razao_social.setter
    def razao_social(self, value):
        self.nome_razao_social = value

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('sgi_base:pessoajuridica-detail', kwargs={'pk': self.pk})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # pylint: disable=no-member
        self._meta.get_field(
            'nome_razao_social').verbose_name = _('Razão Social')

    def __str__(self):
        return '{nome_razao_social} ({cnpj})'.format(**vars(self))
