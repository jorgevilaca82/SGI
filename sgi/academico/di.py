# coding: utf-8

from injector import Injector, InstanceProvider, Module

from .services.registro_aluno import GeradorRAImpl, GeradorRA, AlunoRAUpdater


class AcademicoModule(Module):

    def configure(self, binder):
        binder.bind(AlunoRAUpdater)
        binder.bind(GeradorRA, to=GeradorRAImpl)


injector = Injector([AcademicoModule, ])
