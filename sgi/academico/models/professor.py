from enum import IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _

from sgi.recursos_humanos import models as rhm


class Professor(rhm.Funcionario):
    
    class Meta:
        pass

    
    class Titulacao(IntEnum):
        GRADUACAO = auto()
        ESPECIALIZACAO = auto()
        MESTRADO = auto()
        DOUTORADO = auto()
        POS_DOUTORADO = auto()

    
    PROFESSOR_TITULACAO_CHOICES = (
        (Titulacao.GRADUACAO.value, _('Gradução')),
        (Titulacao.ESPECIALIZACAO.value, _('Especialização')),
        (Titulacao.MESTRADO.value, _('Mestrador')),
        (Titulacao.DOUTORADO.value, _('Doutorado')),
        (Titulacao.POS_DOUTORADO.value, _('Pós Doutorado')),
    )

    titulacao = models.IntegerField(choices=PROFESSOR_TITULACAO_CHOICES)
