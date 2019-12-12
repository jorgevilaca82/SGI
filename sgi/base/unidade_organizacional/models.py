from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.exceptions import ValidationError

from sgi.commons.models import AuditableModel
from sgi.base import models as bm


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

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True)

    object_id = models.PositiveIntegerField(null=True)

    content_object = GenericForeignKey('content_type', 'object_id')

    sub_uos = GenericRelation('UnidadeOrganizacional')

    def __str__(self):
        return '{0} > {1}'.format(self.uo_superior or self.pessoa_juridica.razao_social, self.sigla)
    

    def clean(self):
        if not self.pessoa_juridica and not self.uo_superior:
            raise ValidationError('Unidade Organizacional deve estar atrelada à uma pessoa jurídica ou à uma unidade organizacional superior.')
