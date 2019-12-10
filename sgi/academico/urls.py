from django.urls import path, include
from django.views import generic
from . import views


app_name = 'academico'

base_module = 'sgi.academico'

home_view = generic.TemplateView.as_view(template_name='academico/home.html')

urlpatterns = [
    path('', home_view, name='home'),
    path('aluno/', home_view, name='aluno-list'),
    path('professor/', home_view, name='professor-list'),
    path('area_capes/search', views.AreaCAPESSearchListView.as_view(), name='area-capes-search-list'),
]
