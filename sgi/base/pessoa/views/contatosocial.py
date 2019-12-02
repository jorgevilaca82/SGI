from sgi.base import models as bm
from sgi.base.pessoa import forms
from . import generic


MODEL = bm.ContatoSocial


class ListView(generic.ListView):
    model = MODEL


class CreateView(generic.CreateView):
    model = MODEL
    form_class = forms.ContatoSocialForm
    success_message = model._meta.verbose_name + \
        " %(tipo)s %(valor)s cadastrado com sucesso!"

    contatos_disabled = []

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'contatos_disabled': self.contatos_disabled})
        return kwargs

    def get(self, request, *args, **kwargs):
        # Desabilita os tipos de contatos já utlizados pela pessoa
        self.contatos_disabled = (
            [contato['tipo']
                for contato in self.pessoa.base_contatosocial_related.values('tipo')])

        return super().get(request, *args, **kwargs)


class DetailView(generic.DetailView):
    model = MODEL


class UpdateView(generic.UpdateView):
    model = MODEL
    form_class = forms.ContatoSocialForm
    success_message = model._meta.verbose_name + \
        " %(tipo)s %(valor)s atualizada com sucesso!"


class DeleteView(generic.DeleteView):
    model = MODEL
    success_message = model._meta.verbose_name + \
        " %(tipo)s %(valor)s excluída permanentemente!"
    success_url_name = 'base:pessoa-conatosocial-list'
