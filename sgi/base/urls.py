from django.urls import include, path

from . import views
from .pessoa import urls as pessoa_urls
from .pessoafisica import urls as pessoafisica_urls
from .pessoajuridica import urls as pessoajuridica_urls
from .unidade_organizacional import urls as unidade_organizacional_urls
from .geo import urls as geo_urls

app_name = "sgi_base"

base_module = "sgi.base"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("pessoafisica/", include(pessoafisica_urls)),
    path("pessoajuridica/", include(pessoajuridica_urls)),
    path("pessoa/", include(pessoa_urls)),
    path("unidade_organizacional/", include(unidade_organizacional_urls)),
    path("geo/", include(geo_urls)),
    # path('reviews/', include((pessoa_urls, 'reviews'), namespace='reviews')),
]
