from rest_framework import serializers
from .models import Registro, AlimentoConsumido
from alimentos.serializers import AlimentoSerializer

class AlimentoConsumidoSerializer(serializers.ModelSerializer): 
    # Traer los detalles completos del alimento en lugar de solo el ID
    alimento_detalle = AlimentoSerializer(source='alimento', read_only=True)
    nombre_alimento = serializers.ReadOnlyField(source='alimento.nombre')

    class Meta:
        model = AlimentoConsumido
        fields = [
            'id',
            'alimento',
            'alimento_detalle',
            'nombre_alimento',
            'cantidad_gramos'
        ]

class RegistroSerializer(serializers.ModelSerializer): 
    username = serializers.ReadOnlyField(source='usuario.username')
    alimentos_consumidos = AlimentoConsumidoSerializer(many=True, read_only=True)

    class Meta: 
        model = Registro
        fields = [
            'id',
            'usuario',
            'username',
            'fecha',
            'comida',
            'alimentos_consumidos'
        ]
        read_only_fields = ['id', 'usuario', 'username']

