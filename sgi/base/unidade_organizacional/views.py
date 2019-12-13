from sgi.base import models as bm
from sgi.commons.views import generic

from . import forms as bf

MODEL = bm.UnidadeOrganizacional
FORM_CLASS = bf.UnidadeOrganizacionalForm


class ListView(generic.ListView):
    model = MODEL


class CreateView(generic.CreateView):
    model = MODEL
    form_class = FORM_CLASS
    success_message = model._meta.verbose_name + \
        " com as sigla %(sigla)s cadastrada com sucesso!"
    template_name = 'base/generic_form.html'


class DetailView(generic.DetailView):
    model = MODEL
    template_name = 'base/unidadeorganizacional_detail.html'


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = FORM_CLASS
    success_message = model._meta.verbose_name + \
        " com sigla %(sigla)s atualizada com sucesso!"
    template_name = 'base/generic_form.html'


class DeleteView(generic.DeleteView):
    model = MODEL
    success_message = model._meta.verbose_name + \
        " com sigla %(sigla)s excluída permanentemente!"
    success_url_name = 'sgi_base:unidadeorganizacional-list'
