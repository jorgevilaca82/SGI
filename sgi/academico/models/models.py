from enum import IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _

from sgi.administracao import models as adm
from sgi.base import models as bm
from sgi.recursos_humanos import models as rhm

from .processo_seletivo.models import *  # no-qa


class Aluno(models.Model):
    """
    A Pessoa Física só se torna um aluno quando está devidamente
    associada um curso. Uma Pessoa Física pode ser aluno de mais de um curso,
    mas nunca mais que dois e sem conflito de turnos
    """

    class Status(IntEnum):
        MATRICULADO = auto()
        EVADIDO = auto()

    ALUNO_STATUS_CHOICES = (
        (Status.MATRICULADO.value, _('Matriculado')),
        (Status.EVADIDO.value, _('Evadido')),
    )

    status = models.IntegerField(choices=ALUNO_STATUS_CHOICES)

    # RA - Registro de Aluno (identificador de matricula)
    ra = models.CharField(max_length=255)
    pessoa_fisica = models.ForeignKey(
        bm.PessoaFisica, on_delete=models.PROTECT)


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


class Curso(models.Model):
    class Meta:
        pass

    # Diretoria de Ensino (de)
    ae = models.ForeignKey(AreaUnidadeDeEnsino, on_delete=models.PROTECT)
