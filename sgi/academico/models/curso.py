from django.db import models


class AreaCAPES(models.Model):
    
    class Meta:
        pass

    codigo = models.PositiveIntegerField(primary_key=True)
    
    descricao = models.CharField(max_length=80)

    @property
    def area_capes(self):
        return "(%s) %s" % (self.codigo, self.descricao)

    def __str__(self):
        return self.area_capes
     