from django.urls import path, include
from django.views import generic
from . import views
from .views import area_capes as ac_views
from .views import unidade_de_ensino as ue_views


app_name = 'academico'

base_module = 'sgi.academico'

home_view = generic.TemplateView.as_view(template_name='academico/home.html')

urlpatterns = [
    path('', home_view, name='home'),
    path('aluno/', home_view, name='aluno-list'),
    path('professor/', home_view, name='professor-list'),
    path('area_capes/search', ac_views.AreaCAPESSearchListView.as_view(), name='area-capes-search-list'),

    path('unidade-de-ensino/', include([

        path('',
                ue_views.ListView.as_view(),
                name='unidade-de-ensino-list'),

        path('create',
                ue_views.CreateView.as_view(),
                name='unidade-de-ensino-create'),

        path('<int:pk>/',
                ue_views.DetailView.as_view(),
                name='unidade-de-ensino-detail'),

        path('<int:pk>/edit',
                ue_views.UpdateView.as_view(),
                name='unidade-de-ensino-update'),

        path('<int:pk>/del',
                views.unidade_de_ensino.DeleteView.as_view(),
                name='unidade-de-ensino-delete'),

    ])),
]
