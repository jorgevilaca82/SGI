from sgi.base import models as bm
from sgi.base.pessoa import forms

from . import generic

MODEL = bm.DocumentoPessoal
FORM_CLASS = forms.DocumentoForm


class ListView(generic.ListView):
    model = MODEL


class CreateView(generic.CreateView):
    model = MODEL
    form_class = FORM_CLASS
    success_message = model._meta.verbose_name + \
        " com n. %(valor)s cadastrado com sucesso!"

    documentos_disabled = []

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'documentos_disabled': self.documentos_disabled})
        return kwargs

    def get(self, request, *args, **kwargs):
        # Desabilita os tipos de documentos já utlizados pela pessoa
        self.documentos_disabled = (
            [documento['tipo']
                for documento in self.pessoa.base_documentopessoal_related.values('tipo')])

        return super().get(request, *args, **kwargs)


class DetailView(generic.DetailView):
    model = MODEL


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = FORM_CLASS
    success_message = model._meta.verbose_name + \
        " com n. %(valor)s atualizada com sucesso!"


class DeleteView(generic.DeleteView):
    model = MODEL
    success_message = model._meta.verbose_name + \
        " com n. %(valor)s excluída permanentemente!"
    success_url_name = 'sgi_base:pessoa-documento-list'
