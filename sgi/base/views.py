from django.http import HttpResponse
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = "base/home.html"
