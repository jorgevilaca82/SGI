from django.urls import path, include
from django.views import generic
from . import views
from .views import area_capes as ac_views
from .views import unidade_de_ensino as ue_views
from sgi.commons.url_utils import crud

app_name = 'academico'

base_module = 'sgi.academico'

home_view = generic.TemplateView.as_view(template_name='academico/home.html')





urlpatterns = [
    path('', home_view, name='home'),
    path('aluno/', home_view, name='aluno-list'),
    path('professor/', home_view, name='professor-list'),
    path('area_capes/search', ac_views.AreaCAPESSearchListView.as_view(), name='area-capes-search-list'),

    crud('unidades-de-ensino', ue_views, url_prefix='unidades-de-ensino'),
]
