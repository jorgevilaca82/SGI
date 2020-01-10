from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from sgi.commons.messages.views import SuccessMessageOnDeleteMixin


class ModelOptsMixin(object):
    def get_context_data(self, **kwargs):
        kwargs['opts'] = self.model._meta
        return super().get_context_data(**kwargs)


class ListView(LoginRequiredMixin, ModelOptsMixin, generic.ListView):
    paginate_by = 5
    ordering = ['-id']


class CreateView(
        LoginRequiredMixin,
        SuccessMessageMixin,
        ModelOptsMixin,
        generic.CreateView):
    extra_context = {'action': _('Cadastrar'), }

    def post(self, request, *args, **kwargs):
        self.success_url = request.GET.get('redirect', None)
        return super().post(request, *args, **kwargs)


class DetailView(LoginRequiredMixin, ModelOptsMixin, generic.DetailView):
    pass


class UpdateView(
        LoginRequiredMixin,
        SuccessMessageMixin,
        ModelOptsMixin,
        generic.UpdateView):
    model = None
    extra_context = {'action': _('Editar'), }


class DeleteView(
        LoginRequiredMixin,
        SuccessMessageOnDeleteMixin,
        generic.DeleteView):
    model = None
    success_url_name = None
    success_params = []

    def get_success_params(self):
        kwg = self.kwargs.get
        return dict(map(lambda k: (k, kwg(k, None)), self.success_params))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.success_url_name:
            self.success_url = reverse_lazy(self.success_url_name,
                                            self.get_success_params())
