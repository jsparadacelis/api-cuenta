#Django utilities
from django.db import models
from perfil.models import Perfil


class Transaccion (models.Model):
    tienda = models.CharField(max_length=50)
    perfil = models.ForeignKey(Perfil, related_name='transacciones', on_delete=models.CASCADE)
    valor = models.IntegerField()

    def __str__(self):
        return self.tienda