from .. import models as am
from sgi.commons.views import generic
from django.forms import modelform_factory


MODEL = am.AreaUnidadeDeEnsino
FORM_CLASS = modelform_factory(MODEL, fields='__all__')


class ListView(generic.ListView):
    model = MODEL


class CreateView(generic.CreateView):
    model = MODEL
    form_class = FORM_CLASS
    # pylint: disable=no-member
    success_message = model._meta.verbose_name + \
        " com n. %(id)s cadastrado com sucesso!"


class DetailView(generic.DetailView):
    model = MODEL


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = FORM_CLASS
    # pylint: disable=no-member
    success_message = model._meta.verbose_name + \
        " com n. %(id)s atualizada com sucesso!"


class DeleteView(generic.DeleteView):
    model = MODEL
    # pylint: disable=no-member
    success_message = model._meta.verbose_name + \
        " com n. %(id)s excluída permanentemente!"
    success_url_name = 'academico:area-unidade-de-ensino-list'
