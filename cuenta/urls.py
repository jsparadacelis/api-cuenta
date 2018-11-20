#Django utilities
from django.urls import path
from .views import *

urlpatterns = [
    #Urls for cuenta
    path('', CuentaList.as_view(), name = 'cuenta'), 
    path('<int:pk>', CuentaDetail.as_view(), name = 'cuenta_id'),
    path('add_money', add_money, name = 'add_money'),
    path('set_zero', set_zero, name = 'set_zero'),
    path("list_tran/<int:id>", list_tran, name = 'list_tran')
]
