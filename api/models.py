from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cuenta (models.Model):
    banco = models.CharField(max_length=50)
    fecha = models.DateField(auto_now=True)
    saldo = models.IntegerField(default=10000)
    deposito = models.IntegerField(default=0, null=True )

    def __str__(self):
        return str(self.banco)
    

class Cliente (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.IntegerField()
    usuario = models.OneToOneField("auth.User", on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.nombre

class Perfil (models.Model):
    cuenta = models.ForeignKey("Cuenta", on_delete=models.CASCADE)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    

class Transaccion (models.Model):
    tienda = models.CharField(max_length=50)
    perfil = models.ForeignKey("Perfil", related_name='transacciones', on_delete=models.CASCADE, default=1)
    # cuenta = models.ForeignKey("Cuenta", related_name='transacciones', on_delete=models.CASCADE, default=1)
    valor = models.IntegerField()

    def __str__(self):
        return self.tienda
    
