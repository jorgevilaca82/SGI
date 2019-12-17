from django.urls import path

from . import views

urlpatterns = [

    path('municipio/search', views.MunicipioSearchListView.as_view(),
         name='municipio-search-list'),
]
