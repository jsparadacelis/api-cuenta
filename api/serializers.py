from rest_framework import serializers
from django.db import transaction
from .models import *
from django.contrib.auth.models import User

import sys

class CuentaSerializer(serializers.ModelSerializer):
    # transacciones = serializers.StringRelatedField(many=True)
    class Meta:
        model = Cuenta
        fields = ('id','banco','fecha','saldo')
    
class PerfilSerializer(serializers.ModelSerializer):
    # transacciones = serializers.StringRelatedField(many=True)
    class Meta:
        model = Perfil
        fields = ('id','cuenta','cliente','rol')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id','nombre','apellido','cedula')
        


class TransListSerializer(serializers.ListSerializer):
    class Meta:
        model = Transaccion
        fields = ('id','tienda','perfil','valor',)


class TransaccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaccion
        list_serializer_class = TransListSerializer
        fields = ('id','tienda','perfil','valor')

    @classmethod
    def create(cls, validated_data):
        with transaction.atomic():
            perfil = validated_data["perfil"]
            cuenta = perfil.cuenta
            cuenta.saldo = cuenta.saldo - validated_data["valor"]
            cuenta.save()
            transaccion = Transaccion(
                tienda = validated_data['tienda'], 
                perfil = perfil,
                valor = validated_data["valor"]
            )
            transaccion.save()
        return transaccion

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('id','saldo') 