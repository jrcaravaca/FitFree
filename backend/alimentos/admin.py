from django.contrib import admin
from . models import Alimento

@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin): 
    list_display = ('nombre', 'calorias', 'proteinas', 'carbohidratos', 'grasas', 'origen', 'estado')
    list_filter = ('origen', 'estado')
    search_fields = ('nombre', 'codigo_barras')

    