from enum import Enum, IntEnum, auto

from django.db import models
from django.utils.translation import gettext_lazy as _

from sgi.administracao import models as admm


class SetorEnsino(admm.Setor):
    """
    Setores e sub-setores de uma unidade de ensino
    """

    class Meta:
        # proxy = True
        pass

    class Categoria(Enum):
        ENSINO = "EDU"

    CATEGORIA_DEFAULT = Categoria.ENSINO
