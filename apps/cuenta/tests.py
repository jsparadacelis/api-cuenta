#utilities fron django test
from django.test import TestCase, Client
#utilities fron django rest framework
from rest_framework.test import APIClient

#utilities from python
import json, time
from .models import Cuenta
from .serializers import CuentaSerializer

class CuentaTestCase(TestCase):
    
    def setUp(self):
        cuenta_datos = {
            "banco": "Banco ABC",
            "fecha": time.strftime("%x"),
            "saldo": 500000
        }
        cuenta_test = Cuenta.objects.create(**cuenta_datos)
        self.client_web = Client()
        self.serializer = CuentaSerializer(instance=cuenta_test)
       
    def test_create_cuenta(self):  
        response = self.client_web.get('/cuenta/1')

        response_json = response.content.decode('utf8').replace("'", '"')
        data_response = json.loads(response_json)
        data_response = json.dumps(data_response, indent=4, sort_keys=True)
        data_serialize = json.dumps(self.serializer.data, indent=4, sort_keys=True)
        
        print(data_response)
        print(data_serialize)

        self.assertEqual(data_response,data_serialize)
        self.assertEqual(response.status_code,200)