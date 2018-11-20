from django.urls import path, include
from .views import  root

urlpatterns = [
    path("", root.view_root , name="root")
]
