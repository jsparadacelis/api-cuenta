#DRF Utilities
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

#Django Utilities
from ..models import *
from ..serializers import *
from django.http import HttpResponse, Http404
from django.shortcuts import render

#Get a collection of Perfil
class PerfilList(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilDetail(APIView):
    def get_object(self, pk):
        try:
            return Perfil.objects.get(pk=pk)
        except Perfil.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = PerfilSerializer(perfil)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        perfil = self.get_object(pk)
        perfil.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = PerfilSerializer(perfil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)