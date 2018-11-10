from django.urls import path, include
from .views import transaccion, cuenta, perfil, cliente, root

urlpatterns = [
    #Urls for cuenta
    path('cuenta/', cuenta.CuentaList.as_view(), name = 'cuenta'), 
    path('cuenta/<int:pk>', cuenta.CuentaDetail.as_view(), name = 'cuenta_id'),

    path('add_money/', cuenta.add_money, name = 'add_money'),
    path('set_zero/', cuenta.set_zero, name = 'set_zero'),
    path("list_tran/<int:id>", cuenta.list_tran, name = 'list_tran'),

    #Urls for transaccion
    path('transaccion/', transaccion.TransaccionList.as_view(), name = 'transaccion'),
    path('transaccion/<int:pk>', transaccion.TransaccionDetail.as_view(), name = 'transaccion_id'),

    #Urls for perfil
    path('perfil/', perfil.PerfilList.as_view(), name = 'perfil'),
    path('perfil/<int:pk>', perfil.PerfilDetail.as_view(), name = 'perfil_id'),
    
    #Urls for cliente
    path('cliente/', cliente.ClienteList.as_view(), name = 'cliente'),
    path('cliente/<int:pk>', cliente.ClienteDetail.as_view(), name = 'cliente_id'),

    path("", root.view_root , name="root")
]
