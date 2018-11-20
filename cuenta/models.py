#Django utilities
from django.db import models

class Cuenta (models.Model):
    banco = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=True)
    saldo = models.IntegerField(default=0, blank = False)

    def __str__(self):
        return str(self.banco)
