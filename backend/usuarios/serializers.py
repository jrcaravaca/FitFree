from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PerfilUsuario, ObjetivoUsuario

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='usuario.username')

    class Meta: 
        model = PerfilUsuario
        fields = [
            'id',
            'username',
            'fecha_nacimiento',
            'peso',
            'altura',
            'sexo',
            'nivel_actividad'
        ]
        read_only_fields = ['id', 'username']


class ObjetivoUsuarioSerializer(serializers.ModelSerializer): 
    username = serializers.ReadOnlyField(source='usuario.username')

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


class RegistroUsuarioSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(write_only=True, min_length=8) #write_only, permite recibir la contraseña en el POST pero garantiza que Django jamás la devuelva en la respuesta JSON

    class Meta: 
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data): 
        user = User.objects.create_user(
            username = validated_data['username'],
            email =  validated_data.get('email', ''),
            password=validated_data['password'],
        )
        PerfilUsuario.objects.create(usuario=user)
        ObjetivoUsuario.objects.create(usuario=user)
        return user

    