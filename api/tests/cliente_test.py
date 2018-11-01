#utilities fron django test
from django.test import TestCase, Client
#utilities fron django rest framework
from rest_framework.test import APIClient

#utilities from python
import json
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

        response_json = response.content.decode('utf8').replace("'", '"')
        data_response = json.loads(response_json)
        data_response = json.dumps(data_response, indent=4, sort_keys=True)
        data_serialize = json.dumps(self.serializer.data, indent=4, sort_keys=True)
        
        print(data_response)
        print(data_serialize)

        self.assertEqual(data_response,data_serialize)
        self.assertEqual(response.status_code,200)