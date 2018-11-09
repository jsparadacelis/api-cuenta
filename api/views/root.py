from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import routers
from . import transaccion, cuenta, perfil, cliente, root

router = routers.DefaultRouter()
#
    