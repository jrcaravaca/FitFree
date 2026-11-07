from django.contrib import admin
from .models import PerfilUsuario, ObjetivoUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin): 
    list_display = ('usuario', 'fecha_nacimiento', 'peso', 'altura', 'sexo', 'nivel_actividad')
    search_fields = ('usuario__username', 'usuario__email',)

@admin.register(ObjetivoUsuario)
class ObjetivoUsuarioAdmin(admin.ModelAdmin): 
    list_display = ('usuario', 'calorias', 'proteinas', 'carbohidratos', 'grasas')
    search_fields = ('usuario__username',)
    