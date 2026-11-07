from django.contrib import admin
from .models import Registro, AlimentoConsumido 

class AlimentoConsumidoInline(admin.TabularInline): 
    model = AlimentoConsumido
    extra = 1

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin): 
    list_display = ('usuario', 'comida', 'fecha')
    list_filter = ('comida', 'fecha')
    search_fields = ('usuario__username',)
    inlines =  [AlimentoConsumidoInline]