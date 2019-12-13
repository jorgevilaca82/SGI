from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django.forms import ModelForm, modelform_factory
from django.utils.translation import gettext_lazy as _

from . import models as bm


class UnidadeOrganizacionalForm(ModelForm):

    class Meta:

        model = bm.UnidadeOrganizacional

        fields = ('sigla',
                  'nome',
                  'pessoa_juridica',)
