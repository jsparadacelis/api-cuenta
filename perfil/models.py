#Django utilities
from django.db import models
from cuenta.models import Cuenta
from cliente.models import Cliente

class Perfil (models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
