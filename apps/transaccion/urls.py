from django.urls import path, include
from .views import *

urlpatterns = [
    #Urls for transaccion
    path('', TransaccionList.as_view(), name = 'transaccion'),
    path('<int:pk>', TransaccionDetail.as_view(), name = 'transaccion_id'),
]
