from django.db.models import Q, QuerySet

from . import models as m


class GeoService(object):
    
    @staticmethod
    def search_municipio_by_nome_or_uf(term: str) -> QuerySet:

        qs = m.Municipio.objects.filter(
            Q(nome__startswith=term) |
            Q(codigo_uf__nome__startswith=term) |
            Q(codigo_uf__uf__startswith=term) 
        )

        return qs
