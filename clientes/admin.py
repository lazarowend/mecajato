from django.contrib import admin
from .models import Cliente, Carro

# Register your models here.
admin.site.register(Carro)
admin.site.register(Cliente)