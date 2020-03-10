from enum import IntEnum, auto

from django.db import models

from .setor_ensino import SetorEnsino


class AreaCAPES(models.Model):
    class Meta:
        pass

    codigo = models.PositiveIntegerField(primary_key=True)

    descricao = models.CharField(max_length=80)

    @property
    def area_capes(self):
        return "(%s) %s" % (self.codigo, self.descricao)

    def __str__(self):
        return self.area_capes


class Curso(models.Model):
    class Meta:
        pass

    # Diretoria de Ensino (de)
    # TODO: analisar a necessidade dessa relação
    de = models.ForeignKey(SetorEnsino, on_delete=models.PROTECT)

    area_capes = models.ForeignKey(AreaCAPES, on_delete=models.PROTECT)


class MatrizCurricular(models.Model):
    """
    Conjunto de discplinas de um curso
    """

    class Meta:
        pass

    class Status(IntEnum):
        ATIVA = auto()
        VIGENTE = auto()
