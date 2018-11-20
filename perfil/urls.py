from django.urls import path, include
from .views import *

urlpatterns = [
   
    #Urls for perfil
    path('', PerfilList.as_view(), name = 'perfil'),
    path('<int:pk>', PerfilDetail.as_view(), name = 'perfil_id'),

]
