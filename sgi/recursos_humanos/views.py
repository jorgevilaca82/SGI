from django.views.generic import ListView

from . import models as rhm


class ServidorPublicoListView(ListView):
    paginate_by = 20
    queryset = rhm.Funcionario.servidores.all()

    model_verbose_name = rhm.Funcionario.get_display_of_tipo(
        rhm.Funcionario.Tipo.SERVIDOR_PUBLICO)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_verbose_name'] = self.model_verbose_name
        return context
