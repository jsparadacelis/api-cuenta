from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cuenta)
admin.site.register(Cliente)
admin.site.register(Perfil)
admin.site.register(Transaccion)