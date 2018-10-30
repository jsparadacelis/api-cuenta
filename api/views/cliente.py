from django.shortcuts import render

# Create your views here.

#DRF Utilities
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

#Django Utilities
from ..models import *
from ..serializers import *
from django.http import HttpResponse

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return HttpResponse("status=status.HTTP_204_NO_CONTENT")
    
    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)