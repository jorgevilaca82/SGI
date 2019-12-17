from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django.forms import ModelForm, modelform_factory, Select, ChoiceField
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from . import models as pfm
from ..geo import models as gm


class _PessoaFisicaForm(ModelForm):


    class Meta:
        model = pfm.PessoaFisica

        fields = (
            'cpf',
            'nome_razao_social',
            'sexo',
            'estado_civil',
            'tipo_sanguineo',
            'natural_cidade',
            'nacionalidade',
            'falecido',
        )

        widgets = {
            'natural_cidade': Select(attrs={
                'class': 'sgi-select2', 
                'data-url': reverse_lazy('sgi_base:municipio-search-list'),
                'data-processFn': 'ofMunicipio'
            }),
        }

        labels = {
            'cpf': _('CPF'),
            'nome_razao_social': _('Nome completo'),
            'tipo_sanguineo': _('Tipo Sanguíneo'),
        }

        extra_required = {
            'sexo': True,
            'estado_civil': True,
            'tipo_sanguineo': True,
            'natural_cidade': True,
            'nacionalidade': True,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set extra required fields
        for field, required in self.Meta.extra_required.items():
            self.fields[field].required = required

        # self.fields['natural_cidade'].widgets.choices = []
        # gm.Municipio.objects.filter(codigo_ibge=self.initial['natural_cidade']).all()

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('cpf', css_class='form-group col-md-4 mb-0'),
                Column('nome_razao_social',
                       css_class='form-group col-md-8 mb-0'),
            ),
            Row(
                Column('sexo', css_class='form-group col-md-4 mb-0'),
                Column('estado_civil', css_class='form-group col-md-5 mb-0'),
                Column('tipo_sanguineo', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('nacionalidade', css_class='form-group col-md-3 mb-0'),
                Column('natural_cidade', css_class='form-group col-md-6 mb-0'),
            ),
            'falecido',
            Submit('submit', 'Salvar'),
        )


PessoaFisicaForm = modelform_factory(pfm.PessoaFisica, form=_PessoaFisicaForm)
