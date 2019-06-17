#DRF Utilities
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

#Django Utilities

from .serializers import *
# TO DO get status with DRF
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Local
from ..models import Client, Transaction, Profile, Account


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClienteDetail(APIView):
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClientSerializer(cliente)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClientSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)