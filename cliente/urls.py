from django.urls import path
from .views import *

urlpatterns = [
    #Urls for cliente
    path('', ClienteList.as_view(), name = 'cliente'),
    path('<int:pk>', ClienteDetail.as_view(), name = 'cliente_id'),
]
