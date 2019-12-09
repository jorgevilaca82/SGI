from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms import (modelform_factory, ModelForm, )
from django.utils.translation import gettext_lazy as _

from . import models as bm


class UnidadeOrganizacionalForm(ModelForm):

    class Meta:
        
        model = bm.UnidadeOrganizacional
        
        fields = ('sigla',
                  'nome',
                  'pessoa_juridica',
                  'content_type',
                  'object_id',)
