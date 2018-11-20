#Django utilities
from django.db import models

class Cliente (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.IntegerField()

    def __str__(self):
        return self.nombre