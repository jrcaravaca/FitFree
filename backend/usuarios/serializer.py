from rest_framework import serializers
from .models import PerfilUsuario, ObjetivoUsuario

class PerfilUsuarioSerializer(serlizares.ModelSerializer):
    username = serializers.ReadOnlyFields(source='usuario.username')

    class Meta: 
        model = PerfilUsuario
        fields = [
            'id',
            'username',
            'fecha_nacimiento',
            'peso',
            'altura',
            'sexo',
            'nviel_actividad'
        ]
        read_only_fields = ['id', 'username']


class ObjetivoUsuarioSerializer(serializers.ModelSerializer): 
    username = serializers.ReadOnlyFields(source='usuario.username')

    class Meta: 
        model = ObjetivoUsuario
        fields = [
            'id',
            'username',
            'calorias',
            'proteinas',
            'carbohidratos',
            'grasas'
        ]
        read_only_fields = ['id', 'username']

