import datetime

from injector import inject


class GeradorRA(object):
    
    def gerar(self):
        raise NotImplementedError()


class GeradorRAImpl(GeradorRA):

    model = None

    def gerar(self):
        y = datetime.date.today().year
        return '%s%s' % (y, self.model.pk)


class AlunoRAUpdater(object):

    @inject
    def __init__(self, gerador_ra: GeradorRA, aluno):
        self.gerador_ra = gerador_ra
        self.aluno = aluno
        self.gerador_ra.model = aluno

    def update(self) -> None:
        self.aluno.ra = self.gerador_ra.gerar()
        self.aluno.save(update_fields=['ra'])
