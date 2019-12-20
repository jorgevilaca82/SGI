
from sgi.commons.views import JSONListView, JSONView

from .services import GeoService


class MunicipioSearchListView(JSONListView):

    def get_queryset(self):

        max_limit = 20

        search_term = self.request.GET.get('term', '')

        limit = self.request.GET.get('l', max_limit)

        if limit > max_limit:
            limit = max_limit

        return GeoService.search_municipio_by_nome_or_uf(search_term)[:limit]

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        fields = [
            'nome',
            'codigo_uf__uf',
            'codigo_ibge',
            'latitude',
            'longitude',
            'capital',
        ]

        def tranform(o):
            return dict(
                nome=o[fields[0]],
                uf=o[fields[1]],
                codigo_ibge=o[fields[2]],
                latitude=o[fields[3]],
                longitude=o[fields[4]],
                capital=o[fields[5]],
            )

        data = list(context['object_list'].values(*fields))
        results = list(map(tranform, data))

        return results


class CEPSearchView(JSONView):

    def get_data(self, context):
        cep = self.kwargs.get('cep')

        return GeoService.get_endereco_by_cep(cep)
