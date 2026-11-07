from rest_framework import serializers
from .models import Alimento


class AlimentoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Alimento
        fields = [
            'id',
            'nombre',
            'calorias', 
            'proteinas', 
            'carbohidratos',
            'grasas', 
            'codigo_barras', 
            'origen',
            'estado',
            'foto',
        ]
        read_only_fields = ['id']
