from django.urls import path, include
from .views import view_root

urlpatterns = [
    path("", view_root , name="root")
]
