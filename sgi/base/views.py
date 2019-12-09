from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "base/home.html"
