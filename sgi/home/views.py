from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import calendar


class HomeView(TemplateView):
    template_name = "home/default.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dias_da_semana'] = list(map(
            lambda d: d.capitalize(), list(calendar.day_name)))
        return context
