from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django.forms import ModelForm, modelform_factory
from django.utils.translation import gettext_lazy as _

from . import models as am


class _UnidadeDeEnsinoForm(ModelForm):

    class Meta:
        model = am.UnidadeDeEnsino

        fields = (
            'tipo',
            'sigla',
            'nome',
            'pessoa_juridica',
            # 'unidade_superior',
        )

        labels = {
            'tipo': _('Tipo'),
            'sigla': _('Sigla'),
            'nome': _('Nome'),
            'pessoa_juridica': _('PJ'),
            # 'unidade_superior': _('Unid. Superior'),
        }

        extra_required = {
            'pessoa_juridica': True,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set extra required fields
        for field, required in self.Meta.extra_required.items():
            self.fields[field].required = required

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-4 mb-0'),
                Column('sigla',
                       css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('nome', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('pessoa_juridica', css_class='form-group col-md-3 mb-0'),
                Column('uo_superior', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Salvar'),
        )


UnidadeDeEnsinoForm = modelform_factory(
    am.UnidadeDeEnsino, form=_UnidadeDeEnsinoForm)
