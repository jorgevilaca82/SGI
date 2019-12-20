from django.urls import path

from . import views

urlpatterns = [

    path('municipio/search', views.MunicipioSearchListView.as_view(),
         name='municipio-search-list'),
    
    path('endereco/cep/<str:cep>', views.CEPSearchView.as_view(),
         name='cep-search-list'),
]
