from typing import Dict

from django.db.models import Q, QuerySet

import viacep

from . import models as m

CepResponseDict = Dict[str, str]


class GeoService(object):

    @staticmethod
    def search_municipio_by_nome_or_uf(term: str) -> QuerySet:

        qs = m.Municipio.objects.filter(
            Q(nome__startswith=term) |
            Q(codigo_uf__nome__startswith=term) |
            Q(codigo_uf__uf__startswith=term)
        )

        return qs

    @staticmethod
    def get_endereco_by_cep(cep: str) -> CepResponseDict:
        viacep_obj = viacep.ViaCEP(cep)
        return viacep_obj.getDadosCEP()
