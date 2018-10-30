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

class TransaccionList(generics.ListCreateAPIView):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer

class TransaccionDetail(APIView):
    def get_object(self, pk):
        try:
            return Transaccion.objects.get(pk=pk)
        except Transaccion.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        transaccion = self.get_object(pk)
        serializer = TransaccionSerializer(transaccion)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        transaccion = self.get_object(pk)
        transaccion.delete()
        return HttpResponse("status=status.HTTP_204_NO_CONTENT")
    
    def put(self, request, pk, format=None):
        transaccion = self.get_object(pk)
        serializer = TransaccionSerializer(transaccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        