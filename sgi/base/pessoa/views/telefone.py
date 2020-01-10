from sgi.base import models as bm
from sgi.base.pessoa import forms

from . import generic

MODEL = bm.Telefone
FORM_CLASS = forms.TelefoneForm


class ListView(generic.ListView):
    model = MODEL


class CreateView(generic.CreateView):
    model = MODEL
    form_class = FORM_CLASS
    # pylint: disable=no-member
    success_message = model._meta.verbose_name + \
        " com n. %(numero)s cadastrado com sucesso!"


class DetailView(generic.DetailView):
    model = MODEL


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = FORM_CLASS
    # pylint: disable=no-member
    success_message = model._meta.verbose_name + \
        " com n. %(numero)s atualizada com sucesso!"


class DeleteView(generic.DeleteView):
    model = MODEL
    # pylint: disable=no-member
    success_message = model._meta.verbose_name + \
        " com n. %(numero)s excluída permanentemente!"
    success_url_name = 'sgi_base:pessoa-telefone-list'
