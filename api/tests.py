#utilities fron django test
from django.test import TestCase, Client
#utilities fron django rest framework
from rest_framework.test import APIClient

#utilities from python
import re, time
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteTestCase(TestCase):
    
    def setUp(self):
        cliente_datos = {
            "nombre": "Fabian",
            "apellido": "paez",
            "cedula": 52320657
        }
        cliente_test = Cliente.objects.create(**cliente_datos)
        self.client_web = Client()
        self.serializer = ClienteSerializer(instance=cliente_test)
       
    def test_create_cliente(self):  
        response = self.client_web.get('/cliente/1')
        print(self.serializer.data)
        print(response.content)
        self.assertEqual(response.status_code,200)