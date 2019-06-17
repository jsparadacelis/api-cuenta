#DRF Utilities
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

#Django Utilities
from ..models import Transaction
from .serializers import *
from django.http import HttpResponse, Http404
from django.shortcuts import render


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransaccionSerializer

class TransactionDetail(APIView):
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        transaccion = self.get_object(pk)
        serializer = TransactionSerializer(transaccion)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        transaccion = self.get_object(pk)
        transaccion.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        transaccion = self.get_object(pk)
        serializer = TransactionSerializer(transaccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        