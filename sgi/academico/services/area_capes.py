from django.db.models import Q
from .. import models as m
from django.db.models import QuerySet


class AreaCAPESService(object):
    
    @staticmethod
    def search(term: str) -> QuerySet:
        
        # TODO: Implementar __unaccent lookup para o postgres

        qs = m.AreaCAPES.objects.filter(
            Q(codigo__startswith=term) | 
            Q(descricao__icontains=term)
        )
        
        return qs