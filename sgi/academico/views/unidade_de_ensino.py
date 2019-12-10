from .. import models as am
from sgi.base.views import generic
from django.forms import modelform_factory
from django.views.generic import View

class FormAndModelMixin:
    model = am.UnidadeDeEnsino
    form_class = modelform_factory(model, fields='__all__')


class ListView(FormAndModelMixin, generic.ListView):
    pass


class CreateView(FormAndModelMixin, generic.CreateView):
    success_message = model._meta.verbose_name + \
        " com n. %(id)s cadastrado com sucesso!"


class DetailView(FormAndModelMixin, generic.DetailView):
    pass


class UpdateView(FormAndModelMixin, generic.UpdateView):
    success_message = model._meta.verbose_name + \
        " com n. %(id)s atualizada com sucesso!"


class DeleteView(FormAndModelMixin, generic.DeleteView):
    success_message = model._meta.verbose_name + \
        " com n. %(id)s excluída permanentemente!"
    success_url_name = 'academico:unidade-de-ensino-list'
