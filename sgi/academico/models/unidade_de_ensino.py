from enum import Enum, IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _

from sgi.administracao import models as admm
from sgi.base import models as bm

from .curso import *


class UnidadeDeEnsino(bm.UnidadeOrganizacional):
    class Meta:
        verbose_name = _("Unidade de Ensino")
        verbose_name_plural = _("Unidades de Ensinos")

    class Tipo(IntEnum):
        CAMPUS = auto()
        POLO = auto()
        ESCOLA = auto()

    TIPO_CHOICES = (
        (Tipo.CAMPUS.value, _("Campus")),
        (Tipo.POLO.value, _("Polo")),
        (Tipo.ESCOLA.value, _("Escola")),
    )

    tipo = models.IntegerField(choices=TIPO_CHOICES)

    class PorTipoQuerySet(models.QuerySet):
        def campus(self):
            return self.filter(tipo=UnidadeDeEnsino.Tipo.CAMPUS)

        def escolas(self):
            return self.filter(tipo=UnidadeDeEnsino.Tipo.ESCOLA)

        def polo(self):
            return self.filter(tipo=UnidadeDeEnsino.Tipo.POLO)

    por_tipo = PorTipoQuerySet.as_manager()

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("sgi_academico:unidade-de-ensino-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return super().__str__()

    def clean(self):
        pass
