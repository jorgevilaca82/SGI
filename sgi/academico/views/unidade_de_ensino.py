from sgi.commons.views import generic

from .. import models as am
from ..forms import UnidadeDeEnsinoForm

MODEL = am.UnidadeDeEnsino
FORM_CLASS = UnidadeDeEnsinoForm


class ListView(generic.ListView):
    model = MODEL


class CreateView(generic.CreateView):
    model = MODEL
    form_class = FORM_CLASS
    # pylint: disable=no-member
    success_message = (
        model._meta.verbose_name + " com n. %(sigla)s cadastrado com sucesso!"
    )
    template_name = "base/generic_form.html"


class DetailView(generic.DetailView):
    model = MODEL


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = FORM_CLASS
    # pylint: disable=no-member
    success_message = (
        model._meta.verbose_name + " com n. %(sigla)s atualizada com sucesso!"
    )
    template_name = "base/generic_form.html"


class DeleteView(generic.DeleteView):
    model = MODEL
    # pylint: disable=no-member
    success_message = (
        model._meta.verbose_name + " com n. %(sigla)s excluída permanentemente!"
    )
    success_url_name = "academico:unidade-de-ensino-list"
