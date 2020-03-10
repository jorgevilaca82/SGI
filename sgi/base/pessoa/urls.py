from django.urls import include, path

from sgi.commons.url_utils import crud

from . import views

# base_module = 'sgi.base'

urlpatterns = [
    path(
        "<int:pessoa_id>/",
        include(
            [
                crud("telefone", views.telefone, url_prefix="pessoa-telefone"),
                crud(
                    "contatosocial",
                    views.contatosocial,
                    url_prefix="pessoa-contatosocial",
                ),
                crud("endereco", views.endereco, url_prefix="pessoa-endereco"),
                crud("documento", views.documento, url_prefix="pessoa-documento"),
                crud("documento", views.documento, url_prefix="pessoa-documento"),
            ]
        ),
    ),
]
