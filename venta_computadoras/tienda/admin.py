# tienda/admin.py
from django.contrib import admin
from .models import Computadora

@admin.register(Computadora)
class ComputadoraAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'precio', 'descripcion', 'imagen', 'destacada')  # Muestra 'destacada' en el admin
    list_filter = ('destacada',)  # Agrega filtro por 'destacada' en el admin
