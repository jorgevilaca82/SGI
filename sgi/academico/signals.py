from django.db.models.signals import post_save
from django.dispatch import receiver

from .di import injector
from .models import Aluno
from .services.registro_aluno import AlunoRAUpdater
from injector import ClassAssistedBuilder


def execute_aluno_ra_updater(instance):
    builder = injector.get(ClassAssistedBuilder[AlunoRAUpdater])
    updater = builder.build(aluno=instance)
    updater.update()


@receiver(post_save, sender=Aluno)
def post_save_aluno(sender, **kwargs):
    if kwargs.get("created"):
        execute_aluno_ra_updater(kwargs.get("instance"))
