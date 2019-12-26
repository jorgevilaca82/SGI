from enum import IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _

from sgi.base import models as bm


class Aluno(bm.PessoaFisica):
    """
    A Pessoa Física só se torna um aluno quando está devidamente
    associada um curso. Uma Pessoa Física pode ser aluno de mais de um curso,
    mas nunca mais que dois e sem conflito de turnos
    """

    class Status(IntEnum):
        MATRICULADO = auto()
        EVADIDO = auto()
        TRANCADO = auto()
        JUBILADO = auto()
        CANCELADO = auto()
        EGRESSO = auto()
        FORMADO = auto()
        AFASTADO = auto()
        FALECIDO = auto()

    ALUNO_STATUS_CHOICES = (
        (Status.MATRICULADO.value, _('Matriculado')),
        (Status.EVADIDO.value, _('Evadido')),
        (Status.TRANCADO.value, _('Trancado')),
        (Status.JUBILADO.value, _('Jubilado')),
        (Status.CANCELADO.value, _('Cancelado')),
        (Status.EGRESSO.value, _('Egresso')),
        (Status.FORMADO.value, _('Formado')),
        (Status.AFASTADO.value, _('Afastado')),
        (Status.FALECIDO.value, _('Falecido')),
    )

    status = models.IntegerField(choices=ALUNO_STATUS_CHOICES)

    # RA - Registro de Aluno (identificador de matricula)
    ra = models.CharField(
        max_length=20, default='', editable=False, unique=True)

