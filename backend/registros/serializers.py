from rest_framework import serializers
from .models import Registro, AlimentoConsumido
from alimentos.serializers import AlimentoSerializer

class AlimentoConsumidoSerializer(serializers.ModelSerializer): 
    # Traer los detalles completos del alimento en lugar de solo el ID
    alimento_detalle = AlimentoSerializer(source='alimento', read_only=True)
    nombre_alimento = serializers.ReadOnlyField(source='alimento.nombre')
    macros_calculados = serializers.SerializerMethodField()

    class Meta:
        model = AlimentoConsumido
        fields = [
            'id',
            'alimento',
            'alimento_detalle',
            'nombre_alimento',
            'cantidad_gramos',
            'macros_calculados'
        ]

    def get_macros_calculados(self, obj): 
        factor = float(obj.cantidad_gramos) / 100.0
        return{
            'calorias': round(float(obj.alimento.calorias) * factor, 2),
            'proteinas': round(float(obj.alimento.proteinas) * factor, 2),
            'carbohidratos': round(float(obj.alimento.carbohidratos) * factor, 2),
            'grasas': round(float(obj.alimento.grasas)* factor, 2),
        }


class RegistroSerializer(serializers.ModelSerializer): 
    username = serializers.ReadOnlyField(source='usuario.username')
    alimentos_consumidos = AlimentoConsumidoSerializer(many=True, read_only=True)
    totales_comida = serializers.SerializerMethodField()

    class Meta: 
        model = Registro
        fields = [
            'id',
            'usuario',
            'username',
            'fecha',
            'comida',
            'alimentos_consumidos',
            'totales_comida'
        ]
        read_only_fields = ['id', 'usuario', 'username']
    
    def get_totales_comida(self, obj): 
        totales = {
            'calorias':0.0,
            'proteinas': 0.0,
            'carbohidratos': 0.0,
            'grasas': 0.0
            }

        for item in obj.alimentos_consumidos.all(): 
            factor = float(item.cantidad_gramos) / 100.0
            totales['calorias'] += float(item.alimento.calorias) * factor
            totales['proteinas'] += float(item.alimento.proteinas) * factor
            totales['carbohidratos'] += float(item.alimento.carbohidratos) * factor
            totales['grasas'] += float(item.alimento.grasas) * factor

        return {k: round(v, 2) for k, v in totales.items()}





