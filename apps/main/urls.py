from django.urls import path, include
from .views import *

urlpatterns = [
   
    #Urls for perfil
    path('', PerfilList.as_view(), name = 'perfil'),
    path('<int:pk>', PerfilDetail.as_view(), name = 'perfil_id'),

]

from django.urls import path, include
from .views import *

urlpatterns = [
    #Urls for transaccion
    path('', TransaccionList.as_view(), name = 'transaccion'),
    path('<int:pk>', TransaccionDetail.as_view(), name = 'transaccion_id'),
]

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

from django.urls import path
from .views import *

urlpatterns = [
    #Urls for cliente
    path('', ClienteList.as_view(), name = 'cliente'),
    path('<int:pk>', ClienteDetail.as_view(), name = 'cliente_id'),
]
