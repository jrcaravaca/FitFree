from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import PerfilUsuario, ObjetivoUsuario
from .serializers import PerfilUsuarioSerializer, ObjetivoUsuarioSerializer, RegistroUsuarioSerializer

class RegistroUsuarioView(generics.CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [permissions.AllowAny] #AllowAny, permite crear cuentas nuevas sin tener token de acceso previo


class PerfilUsuarioDetailView(generics.RetrieveUpdateAPIView): 
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self): 
        # Obtiene el  objecto directamente desde self.request.user. Así eliminamos <int:pk> de la URL y evitamos que un usuario pueda editar los datos de otro cambiando el número en la petición 
        perfil, _ = PerfilUsuario.objects.get_or_create(usuario=self.request.user)
        return perfil

class ObjetivoUsuarioDetailView(generics.RetrieveUpdateAPIView): 
    serializer_class = ObjetivoUsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self): 
        objetivo, _ = ObjetivoUsuario.objects.get_or_create(usuario=self.request.user)
        return objetivo





