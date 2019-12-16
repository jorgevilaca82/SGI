from django.db import models


class Estado(models.Model):
    codigo_uf = models.PositiveIntegerField(primary_key=True)
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=140)


class Municipio(models.Model):
    codigo_ibge = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=140)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    capital = models.BooleanField()
    codigo_uf = models.ForeignKey(Estado, on_delete=models.PROTECT)
