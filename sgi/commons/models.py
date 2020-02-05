from django.db import models


class AuditableModel(models.Model):

    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)


class NomeESiglaMixin(object):

    sigla = models.CharField(max_length=20)

    nome = models.CharField(max_length=140)
