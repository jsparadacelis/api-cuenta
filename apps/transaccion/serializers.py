#DRF utilities
from rest_framework import serializers

#Django Utilities
from django.db import transaction
from .models import *

class TransListSerializer(serializers.ListSerializer):
    class Meta:
        model = Transaccion
        fields = ('id','tienda','perfil','valor',)


class TransaccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaccion
        list_serializer_class = TransListSerializer
        fields = ('id','tienda','perfil','valor')

    
    def create(self, validated_data):
        with transaction.atomic():
            perfil = validated_data["perfil"]
            cuenta = perfil.cuenta
            if cuenta.saldo <= 0:
                raise serializers.ValidationError("Fondos insuficientes")


            cuenta.saldo = cuenta.saldo - validated_data["valor"]
            cuenta.save()
            transaccion = Transaccion(
                tienda = validated_data['tienda'], 
                perfil = perfil,
                valor = validated_data["valor"]
            )
            transaccion.save()
        return transaccion
