import calendar

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home/default.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["dias_da_semana"] = list(
            map(lambda d: d.capitalize(), list(calendar.day_name))
        )

        context["meses"] = list(
            map(lambda m: m.capitalize(), list(calendar.month_name))
        )

        return context
