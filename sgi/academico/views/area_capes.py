
from sgi.commons.views import JSONListView
# from django.db.models import Q
# from . import models as m
from ..services.area_capes import AreaCAPESService


class AreaCAPESSearchListView(JSONListView):

    
    def get_queryset(self):

        max_limit = 20

        search_term = self.request.GET.get('term', '')
        
        limit = self.request.GET.get('l', max_limit)
        
        if limit > max_limit:
            limit = max_limit
        
        return AreaCAPESService.search(search_term)[:limit]

    
    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        fields = ['codigo', 'descricao']
        
        data = list(context['object_list'].values(*fields))

        return dict(data=data)