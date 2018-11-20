#DRF Utilities
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

#Django Utilities
from ..models import *
from ..serializers import *
from django.http import HttpResponse, Http404
from django.db import connection
from django.shortcuts import render

#Get a collection of Cuentas
class CuentaList(generics.ListCreateAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

#Get a cuenta
class CuentaDetail(APIView):
    @classmethod
    def get_object(cls, pk):
        try:
            return Cuenta.objects.select_for_update().get(pk=pk)
        except Cuenta.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        cuenta = self.get_object(pk)
        serializer = CuentaSerializer(cuenta)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        cuenta = self.get_object(pk)
        cuenta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        cuenta = self.get_object(pk)
        serializer = CuentaSerializer(cuenta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def add_money(request):
    if request.method == 'PUT':
        try:
            cuenta = Cuenta.objects.get(pk = request.data["id"])
            cuenta.saldo += request.data["deposit"]
            serializerResponse = CuentaSerializer(cuenta)
            serializer = SaldoSerializer(cuenta, data = request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializerResponse.data)
        except KeyError:
            return Response("Invalid key")
        except Cuenta.DoesNotExist:
            raise Http404("Account doesn't exist")
            

    
@api_view(['PUT'])
def set_zero(request):
    if request.method == 'PUT':
        try:
            cuenta = Cuenta.objects.get(pk = request.data["id"])
            cuenta.saldo = 0
            serializerResponse = CuentaSerializer(cuenta)
            serializer = SaldoSerializer(cuenta, data = request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializerResponse.data)
        except KeyError:
            return Response("Invalid key")
        except Cuenta.DoesNotExist:
            raise Http404("Account doesn't exist")
        

@api_view(['GET'])
def list_tran(request, id):
        if request.method == 'GET':
            try:
                cuenta = Cuenta.objects.get(pk = id)
                perfil = Perfil.objects.filter(cuenta_id = cuenta.id)
                lista_trans = [Transaccion.objects.filter(perfil_id = p.id) for p in perfil]

                list_serializer = [TransaccionSerializer(lista, many = True) for lista in lista_trans]
                cuenta_serializer = CuentaSerializer(cuenta)

                list_data = [list_serializer.data for list_serializer in list_serializer]
                list_data.append(cuenta_serializer.data)
                return Response(list_data)
            except Cuenta.DoesNotExist:
                raise Http404("Account doesn't exist")
        else:
            return Response("Unsupported Method")
   
    