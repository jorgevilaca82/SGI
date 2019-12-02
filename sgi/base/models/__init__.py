from sgi.base.pessoa.models import (
    Pessoa,
    ContatoSocial,
    DocumentoPessoalTipo,
    DocumentoPessoal,
    Endereco,
    Telefone
)
from sgi.base.pessoafisica.models import PessoaFisica, RelacaoDependencia
from sgi.base.pessoajuridica.models import PessoaJuridica
from sgi.base.unidade_organizacional.models import UnidadeOrganizacional

__all__ = [
    'Pessoa',
    'Endereco',
    'ContatoSocial',
    'DocumentoPessoalTipo',
    'DocumentoPessoal',
    'Telefone',
    'PessoaJuridica',
    'PessoaFisica',
    'RelacaoDependencia',
    'UnidadeOrganizacional'
]
