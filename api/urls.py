from django.urls import path
from .views import transaccion, cuenta, perfil, cliente

urlpatterns = [
    #Urls for cuenta
    path('cuenta/', cuenta.CuentaList.as_view()), 
    path('cuenta/<int:pk>', cuenta.CuentaDetail.as_view()),
    #For adding money in account
    path('add_money/', cuenta.add_money),
    path('set_zero/', cuenta.set_zero),
    path("list_tran/<int:id>", cuenta.list_tran),
    #Urls for transaccion
    path('transaccion/', transaccion.TransaccionList.as_view()),
    path('transaccion/<int:pk>', transaccion.TransaccionDetail.as_view()),
    #Urls for perfil
    path('perfil/', perfil.PerfilList.as_view()),
    path('perfil/<int:pk>', perfil.PerfilDetail.as_view()),
    #Urls for cliente
    path('cliente/', cliente.ClienteList.as_view()),
    path('cliente/<int:pk>', cliente.ClienteDetail.as_view())
]
